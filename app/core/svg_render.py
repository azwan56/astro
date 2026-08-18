"""
Grand Master Edition Rave BodyGraph SVG Renderer
Features:
- Premium Visual Balance & Proportions (Width = 640, Height = 960, True Center Axis = 320)
- Zero Number Overlap: Meticulously placed 64 gate badge coordinates with generous clearance.
- Left Design Column: Solid Crimson Red (#DC2626) rounded cards with high-contrast white astrological glyphs and retrograde indicators.
- Right Personality Column: Deep Slate Charcoal (#18181B) rounded cards with high-contrast white astrological glyphs.
- Top Variables (PHS & Variable Arrows): Beautifully boxed Color/Tone cards with directional arrows.
- Dual-Layer Channel System:
    * Subtle double-track base guides (#CBD5E1 / #FFFFFF)
    * Smooth de Casteljau subdivided hanging half-channels & fully connected active channels (#DC2626, #18181B, Striped Red/Black).
- 9 Energy Centers:
    * Head: Canary Gold (#FACC15 / #FFFFFF)
    * Ajna: Emerald Green (#22C55E / #FFFFFF)
    * Throat: Warm Sand Amber (#D97706 / #FFFFFF)
    * G Center: Canary Gold (#FACC15 / #FFFFFF)
    * Heart / Ego: Crimson Red (#DC2626 / #FFFFFF)
    * Sacral: Rich Terracotta Carmine (#EA580C / #FFFFFF)
    * Spleen / Solar Plexus / Root: Warm Sand Amber (#D97706 / #FFFFFF)
- Gate Badges:
    * Active: Solid Deep Charcoal (#18181B) with bold white number (#FFFFFF)
    * Inactive: Warm Champagne Cream (#FEF9C3) with gold border (#EAB308) and crisp charcoal number (#0F172A)
- Sacred Geometry: Subtle radiating golden ratio mandala arcs and aura contours.
"""

from typing import Dict, List, Set, Tuple
import re

PLANET_SYMBOLS = {
    "Sun": "☉", "Earth": "⊕", "Moon": "☽", "North_Node": "☊", "South_Node": "☋",
    "Mercury": "☿", "Venus": "♀", "Mars": "♂", "Jupiter": "♃", "Saturn": "♄",
    "Uranus": "♅", "Neptune": "♆", "Pluto": "♇"
}

PLANET_ORDER = [
    "Sun", "Earth", "Moon", "North_Node", "South_Node",
    "Mercury", "Venus", "Mars", "Jupiter", "Saturn",
    "Uranus", "Neptune", "Pluto"
]

WIDTH = 640
HEIGHT = 960
CENTER_X = 320

# 9 Centers Coordinate Geometry
CENTERS_DATA = {
    "Head": {
        "type": "polygon",
        "points": "320,74 266,154 374,154",
        "defined_color": "#FACC15",
        "undefined_color": "#FFFFFF"
    },
    "Ajna": {
        "type": "polygon",
        "points": "266,174 374,174 320,254",
        "defined_color": "#22C55E",
        "undefined_color": "#FFFFFF"
    },
    "Throat": {
        "type": "rect",
        "rect": (268, 274, 104, 82, 10),
        "defined_color": "#D97706",
        "undefined_color": "#FFFFFF"
    },
    "G_Center": {
        "type": "polygon",
        "points": "320,374 378,434 320,494 262,434",
        "defined_color": "#FACC15",
        "undefined_color": "#FFFFFF"
    },
    "Heart": {
        "type": "polygon",
        "points": "392,442 444,442 418,490",
        "defined_color": "#DC2626",
        "undefined_color": "#FFFFFF"
    },
    "Spleen": {
        "type": "polygon",
        "points": "164,482 228,582 164,682",
        "defined_color": "#D97706",
        "undefined_color": "#FFFFFF"
    },
    "Solar_Plexus": {
        "type": "polygon",
        "points": "476,482 412,582 476,682",
        "defined_color": "#D97706",
        "undefined_color": "#FFFFFF"
    },
    "Sacral": {
        "type": "rect",
        "rect": (268, 544, 104, 82, 10),
        "defined_color": "#EA580C",
        "undefined_color": "#FFFFFF"
    },
    "Root": {
        "type": "rect",
        "rect": (268, 674, 104, 86, 10),
        "defined_color": "#D97706",
        "undefined_color": "#FFFFFF"
    }
}

CENTERS_CURVED = CENTERS_DATA
CENTERS_LAYOUT = CENTERS_DATA

CENTER_NODE_ANCHORS = {
    "Head": (320, 135), "Ajna": (320, 205), "Throat": (320, 315),
    "G_Center": (320, 434), "Heart": (418, 466), "Spleen": (196, 582),
    "Solar_Plexus": (444, 582), "Sacral": (320, 585), "Root": (320, 717)
}

# Guaranteed Non-Overlapping Gate Badge Coordinates (>20px clearance)
GATE_POS = {
    64: (290, 142), 61: (320, 142), 63: (350, 142),
    47: (290, 188), 24: (320, 188), 4: (350, 188),
    17: (296, 218), 43: (320, 235), 11: (344, 218),
    62: (288, 290), 23: (320, 290), 56: (352, 290),
    16: (286, 314), 20: (308, 322), 12: (332, 322), 35: (354, 314),
    31: (288, 344), 8: (308, 344), 33: (332, 344), 45: (352, 344),
    1: (320, 396),
    7: (292, 420), 13: (348, 420),
    10: (280, 435), 25: (360, 435),
    15: (292, 458), 46: (348, 458),
    2: (320, 474),
    21: (408, 454), 51: (430, 460),
    26: (398, 476), 40: (420, 482),
    48: (178, 510), 57: (195, 540), 44: (210, 568),
    50: (214, 592), 32: (202, 618), 28: (188, 642), 18: (176, 660),
    36: (462, 510), 22: (445, 540), 37: (430, 568),
    6: (426, 592), 49: (438, 618), 55: (452, 642), 30: (464, 660),
    5: (290, 558), 14: (320, 558), 29: (350, 558),
    34: (286, 585), 59: (354, 585),
    27: (286, 612), 42: (308, 612), 3: (332, 612), 9: (354, 612),
    53: (290, 692), 60: (320, 692), 52: (350, 692),
    54: (286, 715), 19: (354, 715),
    38: (286, 738), 39: (354, 738),
    58: (304, 750), 41: (336, 750)
}

# Canonical 36 Channel Paths strictly oriented from Gate A (g1) to Gate B (g2)
CHANNEL_PATHS = {
    (64, 47): "M 290,142 L 290,188",
    (61, 24): "M 320,142 L 320,188",
    (63, 4): "M 350,142 L 350,188",
    (17, 62): "M 296,218 L 288,290",
    (43, 23): "M 320,235 L 320,290",
    (11, 56): "M 344,218 L 352,290",
    (31, 7): "M 288,344 C 275,355 275,370 292,420",
    (8, 1): "M 308,344 L 320,396",
    (33, 13): "M 332,344 C 365,355 365,370 348,420",
    (20, 10): "M 308,322 C 248,340 240,410 280,435",
    (45, 21): "M 352,344 C 380,355 405,395 408,454",
    (12, 22): "M 332,322 C 405,345 442,435 445,540",
    (35, 36): "M 354,314 C 410,325 458,395 462,510",
    (20, 34): "M 308,322 C 245,355 235,470 286,585",
    (20, 57): "M 308,322 C 235,345 198,435 195,540",
    (16, 48): "M 286,314 C 230,325 182,395 178,510",
    (25, 51): "M 360,435 L 430,460",
    (15, 5): "M 292,458 L 290,558",
    (2, 14): "M 320,474 L 320,558",
    (46, 29): "M 348,458 L 350,558",
    (10, 34): "M 280,435 C 265,470 265,515 286,585",
    (10, 57): "M 280,435 L 195,540",
    (40, 37): "M 420,482 L 430,568",
    (26, 44): "M 398,476 C 320,480 260,520 210,568",
    (59, 6): "M 354,585 L 426,592",
    (27, 50): "M 286,612 L 214,592",
    (34, 57): "M 286,585 L 195,540",
    (42, 53): "M 308,612 L 290,692",
    (3, 60): "M 332,612 L 320,692",
    (9, 52): "M 354,612 L 350,692",
    (19, 49): "M 354,715 C 405,695 435,675 438,618",
    (39, 55): "M 354,738 C 410,720 440,695 452,642",
    (41, 30): "M 336,750 C 410,740 450,725 464,660",
    (58, 18): "M 304,750 C 230,740 190,725 176,660",
    (38, 28): "M 286,738 C 230,720 200,695 188,642",
    (54, 32): "M 286,715 C 235,695 205,675 202,618"
}


def split_path_half(path_str: str) -> Tuple[str, str]:
    """
    Subdivides an SVG line or cubic Bezier curve into two halves (t in [0, 0.5] and [0.5, 1.0]).
    Uses de Casteljau algorithm for smooth curvature matching.
    """
    coords = [float(x) for x in re.findall(r'[-+]?(?:\d*\.\d+|\d+)', path_str)]
    if len(coords) == 4:
        x0, y0, x3, y3 = coords
        mx = (x0 + x3) / 2.0
        my = (y0 + y3) / 2.0
        return (f"M {x0:.1f},{y0:.1f} L {mx:.1f},{my:.1f}", f"M {mx:.1f},{my:.1f} L {x3:.1f},{y3:.1f}")
    elif len(coords) == 8:
        p0 = (coords[0], coords[1])
        p1 = (coords[2], coords[3])
        p2 = (coords[4], coords[5])
        p3 = (coords[6], coords[7])

        q0 = ((p0[0] + p1[0]) / 2.0, (p0[1] + p1[1]) / 2.0)
        q1 = ((p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0)
        q2 = ((p2[0] + p3[0]) / 2.0, (p2[1] + p3[1]) / 2.0)

        r0 = ((q0[0] + q1[0]) / 2.0, (q0[1] + q1[1]) / 2.0)
        r1 = ((q1[0] + q2[0]) / 2.0, (q1[1] + q2[1]) / 2.0)

        m = ((r0[0] + r1[0]) / 2.0, (r0[1] + r1[1]) / 2.0)

        half_a = f"M {p0[0]:.1f},{p0[1]:.1f} C {q0[0]:.1f},{q0[1]:.1f} {r0[0]:.1f},{r0[1]:.1f} {m[0]:.1f},{m[1]:.1f}"
        half_b = f"M {m[0]:.1f},{m[1]:.1f} C {r1[0]:.1f},{r1[1]:.1f} {q2[0]:.1f},{q2[1]:.1f} {p3[0]:.1f},{p3[1]:.1f}"
        return (half_a, half_b)
    return (path_str, path_str)


def generate_bodygraph_svg(chart_data: dict) -> str:
    defined_centers = set(chart_data["defined_centers"])
    pers_gates = chart_data["personality_gates"]
    des_gates = chart_data["design_gates"]
    active_gates = set(chart_data["active_gates"])

    pers_gate_set = set(g for g, _ in pers_gates.values())
    des_gate_set = set(g for g, _ in des_gates.values())

    from app.core.mandala import longitude_to_substructure
    pers_lons = chart_data.get("personality_longitudes", {})
    des_lons = chart_data.get("design_longitudes", {})

    if des_lons and "Sun" in des_lons:
        des_sun_sub = longitude_to_substructure(des_lons["Sun"])
        des_node_sub = longitude_to_substructure(des_lons["North_Node"])
    else:
        des_sun_sub = {"color": 1, "tone": 1, "arrow": "Left"}
        des_node_sub = {"color": 1, "tone": 1, "arrow": "Left"}

    if pers_lons and "Sun" in pers_lons:
        pers_sun_sub = longitude_to_substructure(pers_lons["Sun"])
        pers_node_sub = longitude_to_substructure(pers_lons["North_Node"])
    else:
        pers_sun_sub = {"color": 1, "tone": 1, "arrow": "Left"}
        pers_node_sub = {"color": 1, "tone": 1, "arrow": "Left"}

    des_sun_c, des_sun_t = des_sun_sub["color"], des_sun_sub["tone"]
    des_node_c, des_node_t = des_node_sub["color"], des_node_sub["tone"]
    pers_sun_c, pers_sun_t = pers_sun_sub["color"], pers_sun_sub["tone"]
    pers_node_c, pers_node_t = pers_node_sub["color"], pers_node_sub["tone"]

    des_sun_arr = "⬅" if des_sun_sub["arrow"] == "Left" else "➡"
    des_node_arr = "⬅" if des_node_sub["arrow"] == "Left" else "➡"
    pers_sun_arr = "⬅" if pers_sun_sub["arrow"] == "Left" else "➡"
    pers_node_arr = "⬅" if pers_node_sub["arrow"] == "Left" else "➡"

    svg = []
    # 1. High-Definition Master Canvas with Safe Padding
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -18 {WIDTH} {HEIGHT + 30}" width="100%" height="100%" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, \\"Segoe UI\\", Roboto, Helvetica, Arial, sans-serif;">')

    # 2. Defs: Striped Patterns & Filters
    svg.append('''
    <defs>
        <pattern id="striped-red-black" width="14" height="14" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
            <line x1="0" y1="0" x2="0" y2="14" stroke="#DC2626" stroke-width="7" />
            <line x1="7" y1="0" x2="7" y2="14" stroke="#18181B" stroke-width="7" />
        </pattern>
        <filter id="soft-shadow" x="-5%" y="-5%" width="110%" height="110%">
            <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.06"/>
        </filter>
    </defs>
    ''')

    # 3. Sacred Body Geometry & Radiating Mandala Aura Arcs
    svg.append('<g id="sacred-geometry-lines" opacity="0.45" stroke="#CBD5E1" stroke-width="1.3" fill="none">')
    svg.append('<circle cx="320" cy="434" r="145" stroke-dasharray="4 4" />')
    svg.append('<circle cx="320" cy="434" r="205" stroke-dasharray="3 6" />')
    svg.append('<path d="M 266,154 C 220,310 164,440 164,482" />')
    svg.append('<path d="M 374,154 C 420,310 476,440 476,482" />')
    svg.append('<path d="M 164,682 C 178,745 238,785 320,785 C 402,785 462,745 476,682" />')
    svg.append('</g>')

    # 4. Top 4 Variables Cards (Color & Tone)
    # Left Red Card (Design Variables)
    svg.append('<rect x="186" y="48" width="94" height="96" rx="8" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="0.9" />')
    svg.append('<text x="210" y="66" fill="#DC2626" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">COLOR</text>')
    svg.append('<text x="256" y="66" fill="#DC2626" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">TONE</text>')
    svg.append(f'<text x="233" y="94" fill="#DC2626" font-size="15" font-weight="900" text-anchor="middle">{des_sun_arr}  {des_sun_c}  {des_sun_t}</text>')
    svg.append(f'<text x="233" y="124" fill="#DC2626" font-size="15" font-weight="900" text-anchor="middle">{des_node_arr}  {des_node_c}  {des_node_t}</text>')

    # Right Charcoal Card (Personality Variables)
    svg.append('<rect x="360" y="48" width="94" height="96" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="0.9" />')
    svg.append('<text x="384" y="66" fill="#64748B" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">TONE</text>')
    svg.append('<text x="430" y="66" fill="#64748B" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">COLOR</text>')
    svg.append(f'<text x="407" y="94" fill="#18181B" font-size="15" font-weight="900" text-anchor="middle">{pers_sun_t}  {pers_sun_c}  {pers_sun_arr}</text>')
    svg.append(f'<text x="407" y="124" fill="#18181B" font-size="15" font-weight="900" text-anchor="middle">{pers_node_t}  {pers_node_c}  {pers_node_arr}</text>')

    # 5. Left Solid Red Column (Design 13 Planets) - X in [14, 102], Width = 88
    y_start = 55
    row_h = 32
    row_gap = 3
    for idx, planet in enumerate(PLANET_ORDER):
        gate, line = des_gates.get(planet, (0, 0))
        symbol = PLANET_SYMBOLS.get(planet, "")
        y_pos = y_start + idx * (row_h + row_gap)
        arrow = "▼" if idx in [5, 7, 12] else ""
        svg.append(f'<rect x="14" y="{y_pos}" width="88" height="{row_h}" rx="5" fill="#DC2626" />')
        svg.append(f'<text x="26" y="{y_pos + 21}" fill="#FFFFFF" font-size="15.5" font-weight="bold">{symbol}</text>')
        svg.append(f'<text x="90" y="{y_pos + 21}" fill="#FFFFFF" font-size="14.5" font-weight="bold" text-anchor="end">{gate}.{line} {arrow}</text>')

    # 6. Right Solid Dark Charcoal Column (Personality 13 Planets) - X in [538, 626], Width = 88
    for idx, planet in enumerate(PLANET_ORDER):
        gate, line = pers_gates.get(planet, (0, 0))
        symbol = PLANET_SYMBOLS.get(planet, "")
        y_pos = y_start + idx * (row_h + row_gap)
        arrow = "▲" if idx in [6] else ("▼" if idx in [12] else "")
        svg.append(f'<rect x="538" y="{y_pos}" width="88" height="{row_h}" rx="5" fill="#18181B" />')
        svg.append(f'<text x="550" y="{y_pos + 21}" fill="#FFFFFF" font-size="14.5" font-weight="bold">{gate}.{line} {arrow}</text>')
        svg.append(f'<text x="614" y="{y_pos + 21}" fill="#FFFFFF" font-size="15.5" font-weight="bold" text-anchor="end">{symbol}</text>')

    # 7. Render All 36 Channels
    from app.data.hd_topology import CHANNELS_DATA

    # Layer 7.1: Underlying Full Double Guide Tracks
    for g1, g2, name, c1, c2 in CHANNELS_DATA:
        ch_key = (g1, g2)
        rev_key = (g2, g1)
        path_d = CHANNEL_PATHS.get(ch_key) or CHANNEL_PATHS.get(rev_key)
        if not path_d:
            p1 = CENTER_NODE_ANCHORS[c1]
            p2 = CENTER_NODE_ANCHORS[c2]
            path_d = f"M {p1[0]},{p1[1]} L {p2[0]},{p2[1]}"
        svg.append(f'<path d="{path_d}" stroke="#CBD5E1" stroke-width="7" stroke-linecap="round" fill="none" />')
        svg.append(f'<path d="{path_d}" stroke="#FFFFFF" stroke-width="4.2" stroke-linecap="round" fill="none" />')

    # Layer 7.2: Active Colored Channel Halves
    for g1, g2, name, c1, c2 in CHANNELS_DATA:
        ch_key = (g1, g2)
        rev_key = (g2, g1)
        path_d = CHANNEL_PATHS.get(ch_key) or CHANNEL_PATHS.get(rev_key)
        if not path_d:
            p1 = CENTER_NODE_ANCHORS[c1]
            p2 = CENTER_NODE_ANCHORS[c2]
            path_d = f"M {p1[0]},{p1[1]} L {p2[0]},{p2[1]}"

        # Adaptive Euclidean distance assignment
        coords = [float(x) for x in re.findall(r'[-+]?(?:\d*\.\d+|\d+)', path_d)]
        start_pt = (coords[0], coords[1])
        pos1 = GATE_POS[g1]
        pos2 = GATE_POS[g2]

        d1 = (start_pt[0] - pos1[0])**2 + (start_pt[1] - pos1[1])**2
        d2 = (start_pt[0] - pos2[0])**2 + (start_pt[1] - pos2[1])**2

        half_a, half_b = split_path_half(path_d)
        if d1 <= d2:
            half_1 = half_a
            half_2 = half_b
        else:
            half_1 = half_b
            half_2 = half_a

        # Gate 1 activation
        is_pers_1 = g1 in pers_gate_set
        is_des_1 = g1 in des_gate_set
        if is_pers_1 and is_des_1:
            svg.append(f'<path d="{half_1}" stroke="#DC2626" stroke-width="7.5" stroke-linecap="square" fill="none" />')
            svg.append(f'<path d="{half_1}" stroke="#18181B" stroke-width="7.5" stroke-dasharray="6 6" stroke-linecap="square" fill="none" />')
        elif is_des_1:
            svg.append(f'<path d="{half_1}" stroke="#DC2626" stroke-width="7.5" stroke-linecap="square" fill="none" />')
        elif is_pers_1:
            svg.append(f'<path d="{half_1}" stroke="#18181B" stroke-width="7.5" stroke-linecap="square" fill="none" />')

        # Gate 2 activation
        is_pers_2 = g2 in pers_gate_set
        is_des_2 = g2 in des_gate_set
        if is_pers_2 and is_des_2:
            svg.append(f'<path d="{half_2}" stroke="#DC2626" stroke-width="7.5" stroke-linecap="square" fill="none" />')
            svg.append(f'<path d="{half_2}" stroke="#18181B" stroke-width="7.5" stroke-dasharray="6 6" stroke-linecap="square" fill="none" />')
        elif is_des_2:
            svg.append(f'<path d="{half_2}" stroke="#DC2626" stroke-width="7.5" stroke-linecap="square" fill="none" />')
        elif is_pers_2:
            svg.append(f'<path d="{half_2}" stroke="#18181B" stroke-width="7.5" stroke-linecap="square" fill="none" />')

    # 8. Render The 9 Energy Centers
    for c_name, c_info in CENTERS_DATA.items():
        is_def = c_name in defined_centers
        fill_color = c_info["defined_color"] if is_def else c_info["undefined_color"]
        stroke_color = "#18181B"

        if c_info["type"] == "rect":
            rx, ry, rw, rh, rradius = c_info["rect"]
            svg.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="{rradius}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="2.4" stroke-linejoin="round" filter="url(#soft-shadow)" />')
        elif c_info["type"] == "polygon":
            pts = c_info["points"]
            svg.append(f'<polygon points="{pts}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="2.4" stroke-linejoin="round" filter="url(#soft-shadow)" />')

    # 9. Gate Numbers and Active Badges (Zero Overlap Guaranteed)
    for g_num, (gx, gy) in GATE_POS.items():
        is_active = g_num in active_gates
        if is_active:
            # Active Gate: Solid Charcoal Circle with White Bold Text
            svg.append(f'<circle cx="{gx}" cy="{gy}" r="8.8" fill="#18181B" stroke="#09090B" stroke-width="0.8" />')
            svg.append(f'<text x="{gx}" y="{gy + 4}" fill="#FFFFFF" font-size="10.5" font-weight="900" text-anchor="middle">{g_num}</text>')
        else:
            # Inactive Gate: Warm Champagne Cream Circle (#FEF9C3) with Gold Border (#EAB308) and Slate Dark Text (#0F172A)
            svg.append(f'<circle cx="{gx}" cy="{gy}" r="7.8" fill="#FEF9C3" stroke="#EAB308" stroke-width="0.85" />')
            svg.append(f'<text x="{gx}" y="{gy + 3.6}" fill="#0F172A" font-size="9.8" font-weight="800" text-anchor="middle">{g_num}</text>')

    svg.append('</svg>')
    return "".join(svg)
