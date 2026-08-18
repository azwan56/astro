"""
Unit Tests for Human Design Engine
"""

import pytest
import datetime
from app.core.mandala import longitude_to_gate_line
from app.core.ephemeris import calculate_planet_longitudes, calculate_design_datetime
from app.core.authority_tree import analyze_human_design_chart


def test_mandala_zero_point():
    # 315° should be Gate 41 Line 1
    gate, line = longitude_to_gate_line(315.0)
    assert gate == 41
    assert line == 1


def test_mandala_gate_span():
    # 315.0 + 5.625 = 320.625 -> Next Gate: Gate 19 Line 1
    gate, line = longitude_to_gate_line(320.625)
    assert gate == 19
    assert line == 1


def test_ephemeris_calculation():
    dt = datetime.datetime(1990, 6, 15, 14, 30, tzinfo=datetime.timezone.utc)
    longitudes = calculate_planet_longitudes(dt)
    
    assert "Sun" in longitudes
    assert "Earth" in longitudes
    assert "Moon" in longitudes
    # Earth must be exactly 180° opposite Sun
    assert abs((longitudes["Earth"] - longitudes["Sun"] + 360) % 360 - 180) < 0.001


def test_design_datetime():
    dt_birth = datetime.datetime(1990, 6, 15, 14, 30, tzinfo=datetime.timezone.utc)
    dt_design, des_lons = calculate_design_datetime(dt_birth)
    pers_lons = calculate_planet_longitudes(dt_birth)
    
    # Design Sun should be approx 88° behind Birth Sun
    diff = (pers_lons["Sun"] - des_lons["Sun"] + 360) % 360
    assert abs(diff - 88.0) < 0.01


def test_authority_determination():
    # Test Generators with Sacral active
    personality_gates = {"Sun": (34, 1), "Earth": (20, 1)}
    design_gates = {"Sun": (57, 1), "Earth": (10, 1)}
    
    chart = analyze_human_design_chart(personality_gates, design_gates)
    assert "Sacral" in chart["defined_centers"]
    assert chart["energy_type"] in ["Manifesting Generator", "Pure Generator"]
