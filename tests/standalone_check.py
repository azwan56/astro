"""
Standalone Engine Verification Script (Pure Standard Library)
Verifies:
1. 315° Mandala Wheel Zero-Point & Span Mapping
2. 9 Centers, 64 Gates & 36 Channels Topology
3. Authority Hierarchy & Energy Type Determination
4. Pure Python SVG BodyGraph Rendering
5. Coaching Text Database Schema Integrity
"""

import os
import sys
import json

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.core.mandala import longitude_to_gate_line, MANDALA_GATES
from app.data.hd_topology import CENTERS, CHANNELS_DATA, GATE_TO_CENTER
from app.core.authority_tree import analyze_human_design_chart
from app.core.svg_render import generate_bodygraph_svg


def test_mandala_zero_point():
    print("Testing Mandala 315° Zero-Point...")
    gate, line = longitude_to_gate_line(315.0)
    assert gate == 41, f"Expected Gate 41, got {gate}"
    assert line == 1, f"Expected Line 1, got {line}"
    
    gate_next, line_next = longitude_to_gate_line(315.0 + 5.625)
    assert gate_next == 19, f"Expected Gate 19, got {gate_next}"
    assert line_next == 1, f"Expected Line 1, got {line_next}"
    print("  [SUCCESS] Mandala 315° math formula verified.")


def test_topology():
    print("Testing 9 Centers & 36 Channels Topology...")
    assert len(CENTERS) == 9, f"Expected 9 centers, got {len(CENTERS)}"
    assert len(CHANNELS_DATA) == 36, f"Expected 36 channels, got {len(CHANNELS_DATA)}"
    assert len(GATE_TO_CENTER) == 64, f"Expected 64 gates, got {len(GATE_TO_CENTER)}"
    print("  [SUCCESS] Topology definitions verified.")


def test_authority_and_type():
    print("Testing Authority Tree & Energy Type Determination...")
    # Test Sacral + Throat connected -> Manifesting Generator
    pers_gates = {"Sun": (34, 1), "Earth": (20, 1)}
    des_gates = {"Sun": (57, 1), "Earth": (10, 1)}
    
    result = analyze_human_design_chart(pers_gates, des_gates)
    
    assert "Sacral" in result["defined_centers"], "Sacral should be defined"
    assert result["energy_type"] in ["Manifesting Generator", "Pure Generator"], f"Unexpected type {result['energy_type']}"
    assert result["authority"] == "Sacral Authority", f"Expected Sacral Authority, got {result['authority']}"
    assert result["profile"] == "1/1", f"Expected profile 1/1, got {result['profile']}"
    
    # Test Emotional Authority precedence
    pers_gates_emo = {"Sun": (6, 1), "Earth": (59, 1)}  # Sacral-Solar Plexus 6-59
    des_gates_emo = {"Sun": (34, 1), "Earth": (20, 1)}
    result_emo = analyze_human_design_chart(pers_gates_emo, des_gates_emo)
    assert "Solar_Plexus" in result_emo["defined_centers"]
    assert result_emo["authority"] == "Emotional Authority", f"Emotional Authority must override Sacral, got {result_emo['authority']}"
    print("  [SUCCESS] Authority Pyramid & Energy Type logic verified.")


def test_svg_generator():
    print("Testing SVG BodyGraph Generation...")
    pers_gates = {"Sun": (34, 1), "Earth": (20, 1)}
    des_gates = {"Sun": (57, 1), "Earth": (10, 1)}
    result = analyze_human_design_chart(pers_gates, des_gates)
    
    svg_out = generate_bodygraph_svg(result)
    assert "<svg" in svg_out and "</svg>" in svg_out, "SVG tags missing"
    assert 'Human Design BodyGraph' in svg_out, "Title text missing in SVG"
    print(f"  [SUCCESS] SVG generated successfully ({len(svg_out)} bytes).")


def test_coach_texts_schema():
    print("Testing Coach Texts Database Integrity...")
    db_path = os.path.join(os.path.dirname(__file__), "..", "app", "db", "coach_texts.json")
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "types" in data and "authorities" in data
    assert "Manifesting Generator" in data["types"]
    assert "Emotional Authority" in data["authorities"]
    print("  [SUCCESS] Coach Texts JSON DB verified.")


if __name__ == "__main__":
    print("=== Starting Standalone Verification ===")
    test_mandala_zero_point()
    test_topology()
    test_authority_and_type()
    test_svg_generator()
    test_coach_texts_schema()
    print("=== ALL STANDALONE VERIFICATIONS PASSED SUCCESSFULLY! ===")
