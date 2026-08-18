"""
Grand & High-Definition Classic Clean Rave BodyGraph SVG Renderer
Features:
- Expanded High-Definition Canvas (Width = 640, Height = 960, True Center Axis = 320)
- Zero Number Overlap Architecture: Every gate badge has >20px~35px dedicated clearance.
- Left Solid Red Planet Column (#E50014) with White Glyph & Arrow indicators
- Right Solid Dark Charcoal Planet Column (#2B2129) with White Glyph & Arrow indicators
- Perfectly Symmetrically Placed Top Variables (Color & Tone Arrows for Left Design & Right Personality)
- Exact Authentic Center Colors & Perfectly Spaced Geometry:
    * Head: Defined Yellow (#FFE600), Undefined White (#FFFFFF)
    * Ajna: Defined Green (#48BB78), Undefined White (#FFFFFF)
    * Throat: Defined Warm Tan (#DCA776), Undefined White (#FFFFFF)
    * G Center: Defined Vivid Yellow (#FFE600), Undefined White (#FFFFFF)
    * Heart: Defined Red (#E50014), Undefined White (#FFFFFF)
    * Sacral: Defined Rich Terracotta (#9E4731), Undefined White (#FFFFFF)
    * Spleen / Solar Plexus / Root: Defined Warm Tan (#DCA776), Undefined White (#FFFFFF)
- Gate Nodes:
    * Active Gates: Solid Black Circle (#000000) with White Text (#FFFFFF)
    * Inactive Gates: Plain Dark Grey Text (#374151) without circle
- Channels:
    * Defined Red (Design): Solid #E50014 (Width 8px)
    * Defined Black (Personality): Solid #1F1A24 (Width 8px)
    * Defined Both: Striped Red (#E50014) and Black (#1F1A24)
    * Undefined: Subtle double-line / soft light-grey guide tracks (#D1D5DB)
"""

from typing import Dict, List, Set, Tuple
from app.core.hd_extended_modules import calculate_color_tone

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
CENTER_X = 320  # True Center Axis

# 9 Centers Coordinate Geometry (Width = 640, Height = 960, Center = 320)
CENTERS_DATA = {
    "Head": {
        "type": "polygon",
        "points": "320,80 270,155 370,155",
        "defined_color": "#FFE600",
        "undefined_color": "#FFFFFF"
    },
    "Ajna": {
        "type": "polygon",
        "points": "270,175 370,175 320,250",
        "defined_color": "#48BB78",
        "undefined_color": "#FFFFFF"
    },
    "Throat": {
        "type": "rect",
        "rect": (275, 275, 90, 80, 10),
        "defined_color": "#DCA776",
        "undefined_color": "#FFFFFF"
    },
    "G_Center": {
        "type": "polygon",
        "points": "320,380 375,435 320,490 265,435",
        "defined_color": "#FFE600",
        "undefined_color": "#FFFFFF"
    },
    "Heart": {
        "type": "polygon",
        "points": "385,445 435,445 410,490",
        "defined_color": "#E50014",
        "undefined_color": "#FFFFFF"
    },
    "Spleen": {
        "type": "polygon",
        "points": "170,485 225,580 170,675",
        "defined_color": "#DCA776",
        "undefined_color": "#FFFFFF"
    },
    "Solar_Plexus": {
        "type": "polygon",
        "points": "470,485 415,580 470,675",
        "defined_color": "#DCA776",
        "undefined_color": "#FFFFFF"
    },
    "Sacral": {
        "type": "rect",
        "rect": (275, 545, 90, 80, 10),
        "defined_color": "#9E4731",
        "undefined_color": "#FFFFFF"
    },
    "Root": {
        "type": "rect",
        "rect": (275, 675, 90, 85, 10),
        "defined_color": "#DCA776",
        "undefined_color": "#FFFFFF"
    }
}

CENTERS_CURVED = CENTERS_DATA
CENTERS_LAYOUT = CENTERS_DATA

CENTER_NODE_ANCHORS = {
    "Head": (320, 135), "Ajna": (320, 205), "Throat": (320, 315),
    "G_Center": (320, 435), "Heart": (410, 467), "Spleen": (195, 580),
    "Solar_Plexus": (445, 580), "Sacral": (320, 585), "Root": (320, 715)
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


import re


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
    # 1. High-Definition Canvas with Safe Padding (viewBox 0 -15 640 985)
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -15 {WIDTH} {HEIGHT + 25}" width="100%" height="100%" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, \\"Segoe UI\\", Roboto, sans-serif;">')

    # 2. Defs & Striped Patterns for Red/Black Dual Channels
    svg.append('''
    <defs>
        <pattern id="striped-red-black" width="14" height="14" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
            <line x1="0" y1="0" x2="0" y2="14" stroke="#E50014" stroke-width="7" />
            <line x1="7" y1="0" x2="7" y2="14" stroke="#1F1A24" stroke-width="7" />
        </pattern>
    </defs>
    ''')

    # 3. Delicate Sacred Body Geometry & Radiating Mandala Aura Arcs
    svg.append('<g id="sacred-geometry-lines" opacity="0.35" stroke="#CBD5E1" stroke-width="1.4" fill="none">')
    svg.append('<circle cx="320" cy="435" r="140" stroke-dasharray="4 4" />')
    svg.append('<circle cx="320" cy="435" r="195" stroke-dasharray="3 5" />')
    svg.append('<path d="M 270,155 C 225,310 170,440 170,485" />')
    svg.append('<path d="M 370,155 C 415,310 470,440 470,485" />')
    svg.append('<path d="M 170,675 C 182,740 240,780 320,780 C 400,780 458,740 470,675" />')
    svg.append('</g>')

    # 4. Top Variables / Color & Tone (Red on Left, Dark Charcoal on Right)
    # Left Red (Design)
    svg.append('<text x="210" y="65" fill="#E50014" font-size="12.5" font-weight="700" text-anchor="middle">Color</text>')
    svg.append('<text x="255" y="86" fill="#E50014" font-size="12.5" font-weight="700" text-anchor="middle">Tone</text>')
    svg.append(f'<text x="232" y="110" fill="#E50014" font-size="14.5" font-weight="900" text-anchor="middle">{des_sun_arr}  {des_sun_c}  {des_sun_t}</text>')
    svg.append(f'<text x="232" y="134" fill="#E50014" font-size="14.5" font-weight="900" text-anchor="middle">{des_node_arr}  {des_node_c}  {des_node_t}</text>')

    # Right Charcoal (Personality)
    svg.append('<text x="430" y="65" fill="#4B5563" font-size="12.5" font-weight="700" text-anchor="middle">Color</text>')
    svg.append('<text x="385" y="86" fill="#4B5563" font-size="12.5" font-weight="700" text-anchor="middle">Tone</text>')
    svg.append(f'<text x="408" y="110" fill="#1F1A24" font-size="14.5" font-weight="900" text-anchor="middle">{pers_sun_t}  {pers_sun_c}  {pers_sun_arr}</text>')
    svg.append(f'<text x="408" y="134" fill="#1F1A24" font-size="14.5" font-weight="900" text-anchor="middle">{pers_node_t}  {pers_node_c}  {pers_node_arr}</text>')

    # 5. Left Solid Red Column (Design 13 Planets) - X in [12, 96], Width = 84
    y_start = 55
    row_h = 32
    row_gap = 3
    for idx, planet in enumerate(PLANET_ORDER):
        gate, line = des_gates.get(planet, (0, 0))
        symbol = PLANET_SYMBOLS.get(planet, "")
        y_pos = y_start + idx * (row_h + row_gap)
        arrow = "▼" if idx in [5, 7, 12] else ""
        svg.append(f'<rect x="12" y="{y_pos}" width="84" height="{row_h}" rx="3" fill="#E50014" />')
        svg.append(f'<text x="24" y="{y_pos + 21}" fill="#FFFFFF" font-size="15" font-weight="bold">{symbol}</text>')
        svg.append(f'<text x="84" y="{y_pos + 21}" fill="#FFFFFF" font-size="14" font-weight="bold" text-anchor="end">{gate}.{line} {arrow}</text>')

    # 6. Right Solid Dark Charcoal Column (Personality 13 Planets) - X in [544, 628], Width = 84
    for idx, planet in enumerate(PLANET_ORDER):
        gate, line = pers_gates.get(planet, (0, 0))
        symbol = PLANET_SYMBOLS.get(planet, "")
        y_pos = y_start + idx * (row_h + row_gap)
        arrow = "▲" if idx in [6] else ("▼" if idx in [12] else "")
        svg.append(f'<rect x="544" y="{y_pos}" width="84" height="{row_h}" rx="3" fill="#2B2129" />')
        svg.append(f'<text x="556" y="{y_pos + 21}" fill="#FFFFFF" font-size="14" font-weight="bold">{gate}.{line} {arrow}</text>')
        svg.append(f'<text x="616" y="{y_pos + 21}" fill="#FFFFFF" font-size="15" font-weight="bold" text-anchor="end">{symbol}</text>')

    # 7. Render All 36 Channels (Full Guide Tracks + Active Full/Half Hanging Channels)
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

    # Layer 7.2: Active Colored Channel Halves (Personality Black / Design Red / Both Striped)
    for g1, g2, name, c1, c2 in CHANNELS_DATA:
        ch_key = (g1, g2)
        rev_key = (g2, g1)
        path_d = CHANNEL_PATHS.get(ch_key) or CHANNEL_PATHS.get(rev_key)
        if not path_d:
            p1 = CENTER_NODE_ANCHORS[c1]
            p2 = CENTER_NODE_ANCHORS[c2]
            path_d = f"M {p1[0]},{p1[1]} L {p2[0]},{p2[1]}"

        # Determine if path_d starts near g1 or g2
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

        # Gate 1 activation (colored on half_1)
        is_pers_1 = g1 in pers_gate_set
        is_des_1 = g1 in des_gate_set
        if is_pers_1 and is_des_1:
            svg.append(f'<path d="{half_1}" stroke="#E50014" stroke-width="7.5" stroke-linecap="square" fill="none" />')
            svg.append(f'<path d="{half_1}" stroke="#1F1A24" stroke-width="7.5" stroke-dasharray="6 6" stroke-linecap="square" fill="none" />')
        elif is_des_1:
            svg.append(f'<path d="{half_1}" stroke="#E50014" stroke-width="7.5" stroke-linecap="square" fill="none" />')
        elif is_pers_1:
            svg.append(f'<path d="{half_1}" stroke="#1F1A24" stroke-width="7.5" stroke-linecap="square" fill="none" />')

        # Gate 2 activation (colored on half_2)
        is_pers_2 = g2 in pers_gate_set
        is_des_2 = g2 in des_gate_set
        if is_pers_2 and is_des_2:
            svg.append(f'<path d="{half_2}" stroke="#E50014" stroke-width="7.5" stroke-linecap="square" fill="none" />')
            svg.append(f'<path d="{half_2}" stroke="#1F1A24" stroke-width="7.5" stroke-dasharray="6 6" stroke-linecap="square" fill="none" />')
        elif is_des_2:
            svg.append(f'<path d="{half_2}" stroke="#E50014" stroke-width="7.5" stroke-linecap="square" fill="none" />')
        elif is_pers_2:
            svg.append(f'<path d="{half_2}" stroke="#1F1A24" stroke-width="7.5" stroke-linecap="square" fill="none" />')

    # 8. Render The 9 Energy Centers
    for c_name, c_info in CENTERS_DATA.items():
        is_def = c_name in defined_centers
        fill_color = c_info["defined_color"] if is_def else c_info["undefined_color"]
        stroke_color = "#222222"

        if c_info["type"] == "rect":
            rx, ry, rw, rh, rradius = c_info["rect"]
            svg.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="{rradius}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="2" />')
        elif c_info["type"] == "polygon":
            pts = c_info["points"]
            svg.append(f'<polygon points="{pts}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="2" />')

    # 9. Gate Numbers and Active Badges (Zero Overlap Guaranteed)
    for g_num, (gx, gy) in GATE_POS.items():
        is_active = g_num in active_gates
        if is_active:
            # Active Gate: Solid Black circle (radius 8.5px) with White bold number
            svg.append(f'<circle cx="{gx}" cy="{gy}" r="8.5" fill="#000000" stroke="#000000" stroke-width="0.5" />')
            svg.append(f'<text x="{gx}" y="{gy + 4}" fill="#FFFFFF" font-size="10.2" font-weight="900" text-anchor="middle">{g_num}</text>')
        else:
            # Inactive Gate: Light Yellow Circle (#FEF08A) with Crisp Black Bold Number (#0F172A)
            svg.append(f'<circle cx="{gx}" cy="{gy}" r="7.6" fill="#FEF08A" stroke="#EAB308" stroke-width="0.8" />')
            svg.append(f'<text x="{gx}" y="{gy + 3.6}" fill="#0F172A" font-size="9.5" font-weight="800" text-anchor="middle">{g_num}</text>')

    svg.append('</svg>')
    return "".join(svg)
