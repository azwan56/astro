"""
Commercial Standalone Pure-Python HTTP Server for Human Design Engine
Features:
- Global & China County-Level Geo Search API (/api/v1/geo/search)
- Suspenseful & Rich Main Theme Coaching Engine
- Complete 5-Tier Commercial Membership System
- Quarter & Annual VIP Exclusive Daily Transit Forecast
- Topology Energy Bridge & De-conditioning Diagnostic Engine
"""

import os
import sys
import json
import datetime
import urllib.parse
import pytz
from http.server import HTTPServer, BaseHTTPRequestHandler

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.core.ephemeris import calculate_planet_longitudes, calculate_design_datetime
from app.core.mandala import longitude_to_gate_line
from app.core.authority_tree import analyze_human_design_chart
from app.core.svg_render import generate_bodygraph_svg, PLANET_SYMBOLS, PLANET_ORDER, CENTERS_CURVED as CENTERS_LAYOUT
from app.core.hd_extended_modules import (
    calculate_phs_and_variables, get_gene_keys_data, get_bg5_business_strengths,
    get_psychological_traits, get_dream_rave_data, get_love_and_relationships_data,
    get_penta_team_capabilities, get_energy_bridge_diagnostics, get_daily_transit_coaching,
    get_rich_main_theme_coaching
)
from app.core.ai_coaching import generate_ai_coaching_report
from app.core.geo_db import search_cities, GEO_DATA_LIST
from app.data.hd_topology import GATE_TO_CENTER, CENTERS

STATIC_INDEX_PATH = os.path.join(os.path.dirname(__file__), "app", "static", "index.html")
COACH_TEXTS_PATH = os.path.join(os.path.dirname(__file__), "app", "db", "coach_texts.json")

with open(COACH_TEXTS_PATH, "r", encoding="utf-8") as f:
    COACH_DB = json.load(f)

CENTER_NAMES_CN = {
    "Head": "头脑中心", "Ajna": "逻辑中心", "Throat": "喉咙中心",
    "G_Center": "G中心", "Heart": "意志力/心中心", "Sacral": "荐骨中心",
    "Spleen": "脾/直觉中心", "Solar_Plexus": "情绪中心", "Root": "根部中心"
}


def _get_center_planet_symbols(center_name: str, pers_gates: dict, des_gates: dict) -> list:
    symbols = []
    for planet in PLANET_ORDER:
        g, _ = pers_gates.get(planet, (0, 0))
        if GATE_TO_CENTER.get(g) == center_name:
            symbols.append(PLANET_SYMBOLS.get(planet, ""))
    for planet in PLANET_ORDER:
        g, _ = des_gates.get(planet, (0, 0))
        if GATE_TO_CENTER.get(g) == center_name:
            symbols.append(PLANET_SYMBOLS.get(planet, ""))
    return symbols


class HumanDesignHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        clean_path = parsed_url.path
        if clean_path.startswith("/astro"):
            clean_path = clean_path[6:]
            if not clean_path:
                clean_path = "/"

        if clean_path == "/" or clean_path.startswith("/index"):
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open(STATIC_INDEX_PATH, "rb") as f:
                self.wfile.write(f.read())
        elif clean_path == "/api/v1/geo/search":
            qs = urllib.parse.parse_qs(parsed_url.query)
            q = qs.get("q", [""])[0]
            results = search_cities(q, limit=15)
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success", "query": q, "results": results}, ensure_ascii=False).encode('utf-8'))
        elif clean_path == "/api/v1/geo/all":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(GEO_DATA_LIST, ensure_ascii=False).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length', 0))
        body_data = self.rfile.read(content_len)

        parsed_url = urllib.parse.urlparse(self.path)
        clean_path = parsed_url.path
        if clean_path.startswith("/astro"):
            clean_path = clean_path[6:]
            if not clean_path:
                clean_path = "/"

        if clean_path == "/api/v1/chart/calculate":
            try:
                req_json = json.loads(body_data.decode('utf-8'))
                birth_date_str = req_json.get("birth_date", "1990-06-15")
                birth_time_str = req_json.get("birth_time", "12:00")
                lat = float(req_json.get("latitude", 31.2304))
                lng = float(req_json.get("longitude", 121.4737))
                tz_str = req_json.get("timezone_str", "Asia/Shanghai")
                transit_date_str = req_json.get("transit_date", "")

                unlocked_modules = set(req_json.get("unlocked_modules", []))
                user_tier = req_json.get("user_tier", "FREE")

                try:
                    local_tz = pytz.timezone(tz_str)
                except Exception:
                    local_tz = pytz.UTC

                dt_naive = datetime.datetime.strptime(f"{birth_date_str} {birth_time_str}", "%Y-%m-%d %H:%M")
                dt_local = local_tz.localize(dt_naive)
                dt_utc = dt_local.astimezone(pytz.UTC)

                # 1. Personality
                pers_lons = calculate_planet_longitudes(dt_utc)
                pers_gates = { planet: longitude_to_gate_line(lon) for planet, lon in pers_lons.items() }

                # 2. Design
                dt_design_utc, des_lons = calculate_design_datetime(dt_utc)
                des_gates = { planet: longitude_to_gate_line(lon) for planet, lon in des_lons.items() }

                # 3. Analyze Chart with Bridge Algorithm
                chart_result = analyze_human_design_chart(pers_gates, des_gates)
                chart_result["personality_longitudes"] = pers_lons
                chart_result["design_longitudes"] = des_lons

                # 4. Generate SVG
                svg_str = generate_bodygraph_svg(chart_result)

                # 5. Calculate Extended Modules, Rich Main Theme & Daily Transit Forecast
                phs_var_data = calculate_phs_and_variables(pers_lons, des_lons)
                gene_keys_list = get_gene_keys_data(chart_result["active_gates"])
                bg5_data = get_bg5_business_strengths(chart_result["defined_centers"], chart_result["defined_channels"])
                psych_data = get_psychological_traits(chart_result["defined_centers"], chart_result["undefined_centers"], phs_var_data["variable_code"])
                dream_data = get_dream_rave_data(chart_result["active_gates"])
                love_data = get_love_and_relationships_data(chart_result["active_gates"])
                penta_data = get_penta_team_capabilities(chart_result["active_gates"], chart_result["defined_centers"])

                # Energy Bridge Diagnostics Engine
                bridge_diagnostics = get_energy_bridge_diagnostics(chart_result)

                # Daily Transit Forecast Engine
                daily_transit = get_daily_transit_coaching(chart_result, transit_date_str)

                # Rich Suspenseful Main Theme Generator
                rich_main_theme = get_rich_main_theme_coaching(chart_result)

                channel_details = []
                for ch in chart_result["defined_channels"]:
                    k1 = f"{ch['gate_a']}-{ch['gate_b']}"
                    k2 = f"{ch['gate_b']}-{ch['gate_a']}"
                    c_info = COACH_DB.get("channels", {}).get(k1) or COACH_DB.get("channels", {}).get(k2) or {
                        "name_cn": f"{ch['gate_a']}-{ch['gate_b']} {ch['name']}",
                        "circuit": "能量通道",
                        "desc_cn": f"【{ch['name']}】具备特殊的生命力能量流。"
                    }
                    channel_details.append({
                        "gate_a": ch["gate_a"], "gate_b": ch["gate_b"],
                        "name_cn": c_info["name_cn"], "circuit": c_info.get("circuit", "能量通道"),
                        "desc_cn": c_info["desc_cn"], "color": ch.get("color", "Both")
                    })

                gate_details = []
                for g in chart_result["active_gates"]:
                    g_info = COACH_DB.get("gates", {}).get(str(g)) or {
                        "name_cn": f"{g}号闸门", "desc_cn": f"【{g}号闸门】代表独一无二的天赋。",
                        "shadow_cn": "恐惧", "coaching_question": "我是否在觉察中运用此才能？"
                    }
                    gate_details.append({
                        "gate": g, "name_cn": g_info["name_cn"], "desc_cn": g_info["desc_cn"],
                        "shadow_cn": g_info.get("shadow_cn", ""), "coaching_question": g_info.get("coaching_question", "")
                    })

                defined_centers_rich = [
                    {
                        "center": c, "name_cn": CENTER_NAMES_CN.get(c, c),
                        "planet_symbols": _get_center_planet_symbols(c, pers_gates, des_gates),
                        "desc_cn": COACH_DB.get("centers", {}).get("defined", {}).get(c, f"定义的{CENTER_NAMES_CN.get(c, c)}")
                    } for c in chart_result["defined_centers"]
                ]

                undefined_centers_rich = [
                    {
                        "center": c, "name_cn": CENTER_NAMES_CN.get(c, c),
                        "planet_symbols": _get_center_planet_symbols(c, pers_gates, des_gates),
                        "desc_cn": COACH_DB.get("centers", {}).get("undefined", {}).get(c, f"未定义的{CENTER_NAMES_CN.get(c, c)}")
                    } for c in chart_result["undefined_centers"]
                ]

                profile_key = chart_result["profile"]
                profile_info = COACH_DB.get("profiles", {}).get(profile_key, {"name_cn": f"{profile_key} 人生角色", "theme": "独特性角色"})

                type_info = COACH_DB["types"].get(chart_result["energy_type"], {})
                auth_info = COACH_DB["authorities"].get(chart_result["authority"], {})

                coaching_summary = {
                    "type_cn": type_info.get("name_cn", chart_result["energy_type"]),
                    "aura_cn": type_info.get("aura_cn", ""),
                    "strategy_cn": type_info.get("strategy_cn", chart_result["strategy"]),
                    "key_metric_cn": type_info.get("key_metric_cn", ""),
                    "not_self_theme": type_info.get("not_self_theme", chart_result["not_self_theme"]),
                    "goal_cn": type_info.get("goal_cn", ""),
                    "authority_cn": auth_info.get("name_cn", chart_result["authority"]),
                    "coaching_advice": type_info.get("coaching_advice", "") + " " + auth_info.get("coaching_advice", "")
                }

                user_q = req_json.get("user_question", "")
                chart_full_data = {
                    "energy_type": chart_result["energy_type"], "strategy": chart_result["strategy"],
                    "not_self_theme": chart_result["not_self_theme"], "authority": chart_result["authority"],
                    "profile": chart_result["profile"], "variable_code": phs_var_data["variable_code"],
                    "defined_centers": chart_result["defined_centers"], "undefined_centers": chart_result["undefined_centers"],
                    "defined_channels": chart_result["defined_channels"], "phs_digestion": phs_var_data["phs_digestion"],
                    "coaching_summary": coaching_summary, "channel_details": channel_details,
                    "energy_bridge_diagnostics": bridge_diagnostics, "daily_transit_coaching": daily_transit
                }
                ai_coaching_res = generate_ai_coaching_report(chart_full_data, user_q)

                response_payload = {
                    "status": "success",
                    "birth_utc": dt_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
                    "design_utc": dt_design_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
                    "user_tier": user_tier,
                    "energy_type": chart_result["energy_type"],
                    "strategy": chart_result["strategy"],
                    "signature": chart_result["signature"],
                    "not_self_theme": chart_result["not_self_theme"],
                    "authority": chart_result["authority"],
                    "profile": chart_result["profile"],
                    "profile_info": profile_info,
                    "definition_type": chart_result["definition_type"],
                    "defined_centers": chart_result["defined_centers"],
                    "undefined_centers": chart_result["undefined_centers"],
                    "defined_centers_rich": defined_centers_rich,
                    "undefined_centers_rich": undefined_centers_rich,
                    "defined_channels": chart_result["defined_channels"],
                    "channel_details": channel_details,
                    "gate_details": gate_details,
                    "phs_digestion": phs_var_data["phs_digestion"],
                    "phs_environment": phs_var_data["phs_environment"],
                    "phs_perspective": phs_var_data["phs_perspective"],
                    "phs_motivation": phs_var_data["phs_motivation"],
                    "phs_deconditioning": phs_var_data["phs_deconditioning"],
                    "phs_schedule": phs_var_data["phs_schedule"],
                    "variable_code": phs_var_data["variable_code"],
                    "variable_desc": phs_var_data["variable_desc"],
                    "var_brain_deep": phs_var_data["var_brain_deep"],
                    "var_body_deep": phs_var_data["var_body_deep"],
                    "var_env_deep": phs_var_data["var_env_deep"],
                    "variables": phs_var_data["variables"],
                    "gene_keys": gene_keys_list,
                    "bg5_business": bg5_data,
                    "psychological_traits": psych_data,
                    "dream_rave": dream_data,
                    "love_relationships": love_data,
                    "penta_team": penta_data,
                    "energy_bridge_diagnostics": bridge_diagnostics,
                    "daily_transit_coaching": daily_transit,
                    "rich_main_theme": rich_main_theme,
                    "active_gates": chart_result["active_gates"],
                    "personality_gates": chart_result["personality_gates"],
                    "design_gates": chart_result["design_gates"],
                    "coaching_summary": coaching_summary,
                    "ai_coaching_report": ai_coaching_res,
                    "svg_bodygraph": svg_str,
                    "unlocked_modules": list(unlocked_modules)
                }

                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(response_payload, ensure_ascii=False).encode('utf-8'))
            except Exception as e:
                self.send_response(400)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"detail": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()


def run_server(port=None):
    if port is None:
        port = int(os.environ.get("PORT", 8008))
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, HumanDesignHandler)
    print(f"Server running at http://127.0.0.1:{port}/")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
