"""
Pydantic Models for Human Design API Requests and Responses
"""

from typing import Dict, List, Optional, Tuple
from pydantic import BaseModel, Field


class ChartCalculateRequest(BaseModel):
    birth_date: str = Field(..., example="1990-06-15", description="Birth date YYYY-MM-DD")
    birth_time: str = Field(..., example="14:30", description="Birth time HH:MM (Local Time)")
    latitude: float = Field(..., example=31.2304, description="City Latitude (e.g. Shanghai 31.23)")
    longitude: float = Field(..., example=121.4737, description="City Longitude (e.g. Shanghai 121.47)")
    timezone_str: Optional[str] = Field(None, example="Asia/Shanghai", description="IANA timezone. Auto-detected if omitted.")


class GateActivation(BaseModel):
    gate: int
    line: int


class ChannelInfo(BaseModel):
    gate_a: int
    gate_b: int
    name: str
    center_a: str
    center_b: str
    color: str


class CoachingSummary(BaseModel):
    type_cn: str
    strategy_cn: str
    authority_cn: str
    coaching_advice: str


class ChartCalculateResponse(BaseModel):
    status: str = "success"
    birth_utc: str
    design_utc: str
    energy_type: str
    strategy: str
    signature: str
    not_self_theme: str
    authority: str
    profile: str
    definition_type: str
    defined_centers: List[str]
    undefined_centers: List[str]
    defined_channels: List[ChannelInfo]
    active_gates: List[int]
    personality_gates: Dict[str, Tuple[int, int]]
    design_gates: Dict[str, Tuple[int, int]]
    coaching_summary: CoachingSummary
    svg_bodygraph: str
