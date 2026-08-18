"""
Mandala Wheel Converter
Maps ecliptic longitude (0° - 360°) to Human Design Gate and Line.
Zero point: 315° Ecliptic Longitude = Gate 41 Line 1.
"""

from typing import Tuple

# The 64 Gates sequence along the Rave Mandala Wheel starting at 315.0° (Gate 41)
MANDALA_GATES = [
    41, 19, 13, 49, 30, 55, 37, 63, 22, 36, 25, 17, 21, 51, 42, 3,
    27, 24, 2, 23, 8, 20, 16, 35, 45, 12, 15, 52, 39, 53, 62, 56,
    31, 33, 7, 4, 29, 59, 40, 64, 47, 6, 46, 18, 48, 57, 32, 50,
    28, 44, 1, 43, 14, 34, 9, 5, 26, 11, 10, 58, 38, 54, 60, 61
]

GATE_SPAN_DEG = 5.625      # 360 / 64
LINE_SPAN_DEG = 0.9375     # 5.625 / 6


def longitude_to_gate_line(longitude_deg: float) -> Tuple[int, int]:
    """
    Converts a tropical ecliptic longitude in degrees [0, 360)
    to a Human Design Gate (1-64) and Line (1-6).
    """
    long_normalized = longitude_deg % 360.0
    offset = (long_normalized - 315.0) % 360.0
    
    gate_idx = int(offset // GATE_SPAN_DEG) % 64
    remainder_in_gate = offset % GATE_SPAN_DEG
    
    line_idx = int(remainder_in_gate // LINE_SPAN_DEG) + 1
    if line_idx > 6:
        line_idx = 6
        
    gate = MANDALA_GATES[gate_idx]
    return gate, line_idx
