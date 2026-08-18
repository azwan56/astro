"""
FastAPI Human Design Server & Engine
100% Free, Local, Zero Paid APIs.
"""

import json
import os
import datetime
import pytz
from typing import Tuple
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

try:
    from timezonefinder import TimezoneFinder
    tf = TimezoneFinder()
except Exception:
    tf = None

from app.schemas.hd_models import ChartCalculateRequest, ChartCalculateResponse, CoachingSummary
from app.core.ephemeris import calculate_planet_longitudes, calculate_design_datetime
from app.core.mandala import longitude_to_gate_line
from app.core.authority_tree import analyze_human_design_chart
from app.core.svg_render import generate_bodygraph_svg

app = FastAPI(
    title="Human Design Open Engine API",
    description="Zero-Paid-API Open-Source Human Design Calculation Engine & BodyGraph Generator",
    version="1.0.0"
)

# CORS middleware for Mini Program / Web Frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Coaching Texts DB
COACH_TEXTS_PATH = os.path.join(os.path.dirname(__file__), "db", "coach_texts.json")
with open(COACH_TEXTS_PATH, "r", encoding="utf-8") as f:
    COACH_DB = json.load(f)

STATIC_INDEX_PATH = os.path.join(os.path.dirname(__file__), "static", "index.html")


def _parse_and_convert_to_utc(
    birth_date_str: str,
    birth_time_str: str,
    lat: float,
    lng: float,
    tz_str: str = None
) -> datetime.datetime:
    """
    Parses local birth date and time, resolves timezone, and converts to UTC datetime.
    """
    if not tz_str:
        if tf is not None:
            tz_str = tf.timezone_at(lat=lat, lng=lng)
        if not tz_str:
            tz_str = "Asia/Shanghai"
            
    try:
        local_tz = pytz.timezone(tz_str)
    except Exception:
        local_tz = pytz.UTC
        
    dt_local_naive = datetime.datetime.strptime(f"{birth_date_str} {birth_time_str}", "%Y-%m-%d %H:%M")
    dt_local = local_tz.localize(dt_local_naive)
    dt_utc = dt_local.astimezone(pytz.UTC)
    return dt_utc


@app.get("/")
def root():
    """
    Serves interactive Human Design visualizer UI.
    """
    return FileResponse(STATIC_INDEX_PATH)


@app.post("/api/v1/chart/calculate", response_model=ChartCalculateResponse)
def calculate_chart(req: ChartCalculateRequest):
    """
    Main endpoint for Human Design Chart Calculation & SVG Generation.
    """
    try:
        dt_birth_utc = _parse_and_convert_to_utc(
            req.birth_date, req.birth_time, req.latitude, req.longitude, req.timezone_str
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid date/time or timezone format: {str(e)}")

    # 1. Personality Longitudes & Gates
    pers_longitudes = calculate_planet_longitudes(dt_birth_utc)
    pers_gates = { planet: longitude_to_gate_line(lon) for planet, lon in pers_longitudes.items() }

    # 2. Design Longitudes & Gates (Sun - 88°)
    dt_design_utc, des_longitudes = calculate_design_datetime(dt_birth_utc)
    des_gates = { planet: longitude_to_gate_line(lon) for planet, lon in des_longitudes.items() }

    # 3. Analyze Human Design Chart (Centers, Authority, Type, Channels)
    chart_result = analyze_human_design_chart(pers_gates, des_gates)

    # 4. Generate BodyGraph SVG
    svg_str = generate_bodygraph_svg(chart_result)

    # 5. Extract Coaching Advice
    type_info = COACH_DB["types"].get(chart_result["energy_type"], {})
    auth_info = COACH_DB["authorities"].get(chart_result["authority"], {})
    
    coaching_summary = CoachingSummary(
        type_cn=type_info.get("name_cn", chart_result["energy_type"]),
        strategy_cn=type_info.get("strategy_cn", chart_result["strategy"]),
        authority_cn=auth_info.get("name_cn", chart_result["authority"]),
        coaching_advice=type_info.get("coaching_advice", "") + " " + auth_info.get("coaching_advice", "")
    )

    return ChartCalculateResponse(
        status="success",
        birth_utc=dt_birth_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
        design_utc=dt_design_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
        energy_type=chart_result["energy_type"],
        strategy=chart_result["strategy"],
        signature=chart_result["signature"],
        not_self_theme=chart_result["not_self_theme"],
        authority=chart_result["authority"],
        profile=chart_result["profile"],
        definition_type=chart_result["definition_type"],
        defined_centers=chart_result["defined_centers"],
        undefined_centers=chart_result["undefined_centers"],
        defined_channels=chart_result["defined_channels"],
        active_gates=chart_result["active_gates"],
        personality_gates=chart_result["personality_gates"],
        design_gates=chart_result["design_gates"],
        coaching_summary=coaching_summary,
        svg_bodygraph=svg_str
    )
