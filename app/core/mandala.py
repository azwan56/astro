"""
Official Rave Mandala Wheel Converter
Maps tropical ecliptic longitude (0° - 360°) to Human Design Gate (1-64), Line (1-6), Color (1-6), Tone (1-6), Base (1-5).

Standard Human Design Rave Mandala Zero Point:
Gate 41 Line 1 begins at Aquarius 02° 00' 00" (302.000000° Tropical Ecliptic Longitude).
Each Gate spans 5.625° (360° / 64).
Each Line spans 0.9375° (5.625° / 6).
Each Color spans 0.15625° (0.9375° / 6).
Each Tone spans 0.026041666666666668° (0.15625° / 6).
Each Base spans 0.005208333333333333° (Tone / 5).
"""

from typing import Tuple, Dict, Any

# The exact canonical 64 Gates sequence along the Rave Mandala Wheel starting at Aquarius 02°00'00" (Gate 41)
MANDALA_GATES = [
    41, 19, 13, 49, 30, 55, 37, 63, 22, 36, 25, 17, 21, 51, 42, 3,
    27, 24, 2, 23, 8, 20, 16, 35, 45, 12, 15, 52, 39, 53, 62, 56,
    31, 33, 7, 4, 29, 59, 40, 64, 47, 6, 46, 18, 48, 57, 32, 50,
    28, 44, 1, 43, 14, 34, 9, 5, 26, 11, 10, 58, 38, 54, 61, 60
]

GATE_SPAN_DEG = 360.0 / 64.0                   # 5.625°
LINE_SPAN_DEG = GATE_SPAN_DEG / 6.0            # 0.9375° (56' 15")
COLOR_SPAN_DEG = LINE_SPAN_DEG / 6.0           # 0.15625° (9' 22.5")
TONE_SPAN_DEG = COLOR_SPAN_DEG / 6.0           # 0.026041666666666668° (1' 33.75")
BASE_SPAN_DEG = TONE_SPAN_DEG / 5.0            # 0.005208333333333333° (18.75")
ZERO_POINT_DEG = 302.0000000000                # Aquarius 02° 00' 00"


def longitude_to_gate_line(longitude_deg: float) -> Tuple[int, int]:
    """
    Converts a tropical ecliptic longitude in degrees [0, 360)
    to the official Human Design Gate (1-64) and Line (1-6).
    """
    long_normalized = longitude_deg % 360.0
    offset = (long_normalized - ZERO_POINT_DEG) % 360.0
    
    gate_idx = int(offset // GATE_SPAN_DEG) % 64
    remainder_in_gate = offset % GATE_SPAN_DEG
    
    line_idx = int(remainder_in_gate // LINE_SPAN_DEG) + 1
    if line_idx > 6:
        line_idx = 6
        
    gate = MANDALA_GATES[gate_idx]
    return gate, line_idx


def longitude_to_substructure(longitude_deg: float, is_node: bool = False) -> Dict[str, Any]:
    """
    Converts a tropical ecliptic longitude to complete 5-layer substructure:
    - Gate (1-64)
    - Line (1-6)
    - Color (1-6)
    - Tone (1-6)
    - Base (1-5)
    - Arrow Direction: 'Left' (Tone 1-3) or 'Right' (Tone 4-6)
    """
    long_normalized = longitude_deg % 360.0
    offset = (long_normalized - ZERO_POINT_DEG) % 360.0
    
    gate_idx = int(offset // GATE_SPAN_DEG) % 64
    rem_gate = offset % GATE_SPAN_DEG
    
    line_idx = min(6, int(rem_gate // LINE_SPAN_DEG) + 1)
    rem_line = rem_gate % LINE_SPAN_DEG
    
    if is_node:
        frac_line = 1.0 - (rem_line / LINE_SPAN_DEG)
        color_idx = min(6, int(frac_line * 6) + 1)
        rem_color_frac = (frac_line * 6) % 1.0
        tone_idx = min(6, int(rem_color_frac * 6) + 1)
        rem_tone_frac = (rem_color_frac * 6) % 1.0
        base_idx = min(5, int(rem_tone_frac * 5) + 1)
    else:
        color_idx = min(6, int(rem_line // COLOR_SPAN_DEG) + 1)
        rem_color = rem_line % COLOR_SPAN_DEG
        
        tone_idx = min(6, int(rem_color // TONE_SPAN_DEG) + 1)
        rem_tone = rem_color % TONE_SPAN_DEG
        
        base_idx = min(5, int(rem_tone // BASE_SPAN_DEG) + 1)
    
    arrow = "Left" if tone_idx in [1, 2, 3] else "Right"
    
    return {
        "gate": MANDALA_GATES[gate_idx],
        "line": line_idx,
        "color": color_idx,
        "tone": tone_idx,
        "base": base_idx,
        "arrow": arrow
    }
