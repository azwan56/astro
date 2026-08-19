"""
Sacred Geometry & Meditating Silhouette Human Design BodyGraph SVG Renderer
Inspired by Modern Sacred Geometry, Minimalist Bodyscape & Energy Mandala Flow.

Proportions Harmonized:
- Perfectly unified 9 Centers scale (modular, non-distorted, identical to reference diagram)
- Head/Ajna equilateral triangles (base 68px, height 58px)
- Throat/Sacral/Root balanced rounded squares (66px × 66px, rx 6px)
- G-Center classic diamond (80px × 80px)
- Spleen & Solar Plexus symmetrical lateral triangles (base 100px, width 65px)
- Heart center balanced right-tilted triangle (48px × 48px)
- Full 36 sweeping curved concentric energy channels
- High-contrast gate badges & typography
- Authentic 384-line Rave I Ching fixations & 4 variables
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

WIDTH = 680
HEIGHT = 920
CENTER_X = 340

# 9 Centers Coordinate Geometry (Proportionally Harmonized to Reference Diagram)
CENTERS_DATA = {
    "Head": {
        "type": "polygon",
        "points": "340,56 306,114 374,114",
        "defined_color": "#384556",
        "defined_stroke": "#1E293B",
        "undefined_color": "#FFFFFF",
        "undefined_stroke": "#CBD5E1"
    },
    "Ajna": {
        "type": "polygon",
        "points": "306,146 374,146 340,204",
        "defined_color": "#384556",
        "defined_stroke": "#1E293B",
        "undefined_color": "#FFFFFF",
        "undefined_stroke": "#CBD5E1"
    },
    "Throat": {
        "type": "rect",
        "rect": (307, 240, 66, 66, 6),
        "defined_color": "#384556",
        "defined_stroke": "#1E293B",
        "undefined_color": "#FFFFFF",
        "undefined_stroke": "#CBD5E1"
    },
    "G_Center": {
        "type": "polygon",
        "points": "340,360 380,400 340,440 300,400",
        "defined_color": "#384556",
        "defined_stroke": "#1E293B",
        "undefined_color": "#FFFFFF",
        "undefined_stroke": "#CBD5E1"
    },
    "Heart": {
        "type": "polygon",
        "points": "400,415 448,395 438,455",
        "defined_color": "#9E4741",
        "defined_stroke": "#7F312C",
        "undefined_color": "#FFFFFF",
        "undefined_stroke": "#CBD5E1"
    },
    "Spleen": {
        "type": "polygon",
        "points": "260,485 260,585 195,535",
        "defined_color": "#384556",
        "defined_stroke": "#1E293B",
        "undefined_color": "#FFFFFF",
        "undefined_stroke": "#CBD5E1"
    },
    "Solar_Plexus": {
        "type": "polygon",
        "points": "420,485 420,585 485,535",
        "defined_color": "#9E4741",
        "defined_stroke": "#7F312C",
        "undefined_color": "#FFFFFF",
        "undefined_stroke": "#CBD5E1"
    },
    "Sacral": {
        "type": "rect",
        "rect": (307, 502, 66, 66, 6),
        "defined_color": "#9E4741",
        "defined_stroke": "#7F312C",
        "undefined_color": "#FFFFFF",
        "undefined_stroke": "#CBD5E1"
    },
    "Root": {
        "type": "rect",
        "rect": (307, 630, 66, 66, 6),
        "defined_color": "#9E4741",
        "defined_stroke": "#7F312C",
        "undefined_color": "#FFFFFF",
        "undefined_stroke": "#CBD5E1"
    }
}

CENTERS_CURVED = CENTERS_DATA
CENTERS_LAYOUT = CENTERS_DATA

CENTER_NODE_ANCHORS = {
    "Head": (340, 95), "Ajna": (340, 175), "Throat": (340, 273),
    "G_Center": (340, 400), "Heart": (428, 422), "Spleen": (238, 535),
    "Solar_Plexus": (442, 535), "Sacral": (340, 535), "Root": (340, 663)
}

# 64 Gate Coordinates aligned with the harmonized center boundaries
GATE_POS = {
    # Head Center (306-374, 56-114)
    64: (318, 106), 61: (340, 106), 63: (362, 106),
    # Ajna Center (306-374, 146-204)
    47: (320, 158), 24: (340, 158), 4: (360, 158),
    17: (326, 178), 43: (340, 194), 11: (354, 178),
    # Throat Center (307-373, 240-306)
    62: (318, 252), 23: (340, 252), 56: (362, 252),
    16: (316, 273), 20: (332, 273), 12: (348, 273), 35: (364, 273),
    31: (318, 294), 8: (332, 294), 33: (348, 294), 45: (362, 294),
    # G Center (300-380, 360-440)
    1: (340, 376),
    7: (320, 392), 13: (360, 392),
    10: (312, 400), 25: (368, 400),
    15: (320, 416), 46: (360, 416),
    2: (340, 428),
    # Heart Center (400-448, 395-455)
    21: (412, 412), 51: (436, 405),
    26: (418, 434), 40: (434, 442),
    # Spleen Center (195-260, 485-585)
    48: (208, 515), 57: (222, 502), 44: (248, 500),
    50: (248, 535), 32: (248, 570),
    28: (222, 568), 18: (208, 555),
    # Solar Plexus Center (420-485, 485-585)
    36: (472, 515), 22: (458, 502), 37: (432, 500),
    6: (432, 535), 49: (432, 570),
    55: (458, 568), 30: (472, 555),
    # Sacral Center (307-373, 502-568)
    5: (318, 514), 14: (340, 514), 29: (362, 514),
    34: (316, 535), 59: (364, 535),
    27: (318, 556), 42: (332, 556), 3: (348, 556), 9: (362, 556),
    # Root Center (307-373, 630-696)
    53: (318, 642), 60: (340, 642), 52: (362, 642),
    54: (316, 663), 19: (364, 663),
    38: (318, 684), 39: (362, 684),
    58: (328, 690), 41: (352, 690)
}

GATE_CENTER_MAP = {
    64: 'Head', 61: 'Head', 63: 'Head',
    47: 'Ajna', 24: 'Ajna', 4: 'Ajna', 17: 'Ajna', 43: 'Ajna', 11: 'Ajna',
    62: 'Throat', 23: 'Throat', 56: 'Throat', 16: 'Throat', 20: 'Throat', 31: 'Throat', 8: 'Throat', 33: 'Throat', 12: 'Throat', 35: 'Throat', 45: 'Throat',
    1: 'G_Center', 7: 'G_Center', 13: 'G_Center', 10: 'G_Center', 25: 'G_Center', 15: 'G_Center', 46: 'G_Center', 2: 'G_Center',
    21: 'Heart', 51: 'Heart', 26: 'Heart', 40: 'Heart',
    48: 'Spleen', 57: 'Spleen', 44: 'Spleen', 50: 'Spleen', 32: 'Spleen', 28: 'Spleen', 18: 'Spleen',
    36: 'Solar_Plexus', 22: 'Solar_Plexus', 37: 'Solar_Plexus', 6: 'Solar_Plexus', 49: 'Solar_Plexus', 55: 'Solar_Plexus', 30: 'Solar_Plexus',
    5: 'Sacral', 14: 'Sacral', 29: 'Sacral', 34: 'Sacral', 59: 'Sacral', 27: 'Sacral', 42: 'Sacral', 3: 'Sacral', 9: 'Sacral',
    53: 'Root', 60: 'Root', 52: 'Root', 54: 'Root', 19: 'Root', 38: 'Root', 39: 'Root', 58: 'Root', 41: 'Root'
}

CHANNEL_PATHS = {
    (64, 47): "M 318,106 L 320,158",
    (61, 24): "M 340,106 L 340,158",
    (63, 4): "M 362,106 L 360,158",
    (17, 62): "M 326,178 L 318,252",
    (43, 23): "M 340,194 L 340,252",
    (11, 56): "M 354,178 L 362,252",
    (31, 7): "M 318,294 L 320,392",
    (8, 1): "M 332,294 L 340,376",
    (33, 13): "M 348,294 L 360,392",
    (20, 10): "M 332,273 C 285,295 280,365 312,400",
    (45, 21): "M 362,294 C 390,320 412,370 412,412",
    (12, 22): "M 348,273 C 425,300 465,440 458,502",
    (35, 36): "M 364,273 C 440,290 485,430 472,515",
    (20, 34): "M 332,273 C 280,320 270,460 316,535",
    (20, 57): "M 332,273 C 255,300 215,440 222,502",
    (16, 48): "M 316,273 C 240,290 195,430 208,515",
    (25, 51): "M 368,400 L 436,405",
    (15, 5): "M 320,416 L 318,514",
    (2, 14): "M 340,428 L 340,514",
    (46, 29): "M 360,416 L 362,514",
    (10, 34): "M 312,400 C 295,435 295,490 316,535",
    (10, 57): "M 312,400 L 222,502",
    (40, 37): "M 434,442 L 432,500",
    (26, 44): "M 418,434 C 330,440 280,470 248,500",
    (59, 6): "M 364,535 L 432,535",
    (27, 50): "M 318,556 L 248,535",
    (34, 57): "M 316,535 C 285,530 250,515 222,502",
    (42, 53): "M 332,556 L 318,642",
    (3, 60): "M 348,556 L 340,642",
    (9, 52): "M 362,556 L 362,642",
    (19, 49): "M 364,663 C 415,600 395,630 432,570",
    (39, 55): "M 362,684 C 445,615 415,660 458,568",
    (41, 30): "M 352,690 C 470,640 430,685 472,555",
    (58, 18): "M 328,690 C 210,640 250,685 208,555",
    (38, 28): "M 318,684 C 235,615 265,660 222,568",
    (54, 32): "M 316,663 C 265,600 285,630 248,570"
}


def split_path_half(path_str: str) -> Tuple[str, str]:
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
        des_sun_sub = longitude_to_substructure(des_lons["Sun"], is_node=False)
        des_node_sub = longitude_to_substructure(des_lons["North_Node"], is_node=True)
    else:
        des_sun_sub = {"color": 1, "tone": 1, "arrow": "Left"}
        des_node_sub = {"color": 1, "tone": 6, "arrow": "Right"}

    if pers_lons and "Sun" in pers_lons:
        pers_sun_sub = longitude_to_substructure(pers_lons["Sun"], is_node=False)
        pers_node_sub = longitude_to_substructure(pers_lons["North_Node"], is_node=False)
    else:
        pers_sun_sub = {"color": 1, "tone": 1, "arrow": "Left"}
        pers_node_sub = {"color": 1, "tone": 6, "arrow": "Right"}

    des_sun_arr = "←" if des_sun_sub["arrow"] == "Left" else "→"
    des_node_arr = "←" if des_node_sub["arrow"] == "Left" else "→"
    pers_sun_arr = "←" if pers_sun_sub["arrow"] == "Left" else "→"
    pers_node_arr = "←" if pers_node_sub["arrow"] == "Left" else "→"

    svg = []
    # 1. Master Canvas
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="100%" height="100%" style="background-color: #FAFAFA; font-family: -apple-system, BlinkMacSystemFont, \\"Segoe UI\\", Roboto, Helvetica, Arial, sans-serif;">')

    # 2. Defs: Striped Patterns & Subtle Drop Shadows
    svg.append('''
    <defs>
        <pattern id="striped-red-black" width="14" height="14" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
            <line x1="0" y1="0" x2="0" y2="14" stroke="#DC2626" stroke-width="7" />
            <line x1="7" y1="0" x2="7" y2="14" stroke="#18181B" stroke-width="7" />
        </pattern>
        <filter id="card-shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.06" />
        </filter>
    </defs>
    ''')

    # 3. Sacred Mandala Celestial Grid
    svg.append('<!-- Sacred Mandala Geometry Background Grid -->')
    svg.append('<g opacity="0.65" stroke="#E2E8F0" fill="none">')
    svg.append('<circle cx="340" cy="400" r="140" stroke-width="1.0" />')
    svg.append('<circle cx="340" cy="400" r="230" stroke-width="0.8" stroke-dasharray="4 4" />')
    svg.append('<circle cx="340" cy="400" r="320" stroke-width="1.0" />')
    svg.append('<circle cx="340" cy="400" r="410" stroke-width="0.8" stroke-dasharray="6 6" />')
    svg.append('<line x1="340" y1="20" x2="340" y2="880" stroke-width="1.0" />')
    svg.append('<line x1="140" y1="400" x2="540" y2="400" stroke-width="0.8" stroke-dasharray="4 4" />')
    svg.append('<line x1="160" y1="220" x2="520" y2="580" stroke-width="0.6" stroke-dasharray="4 4" />')
    svg.append('<line x1="160" y1="580" x2="520" y2="220" stroke-width="0.6" stroke-dasharray="4 4" />')
    svg.append('</g>')

    # 4. Zen Meditating Human Silhouette Profile Outline
    silhouette_path = """
    M 340,32
    C 368,32 386,48 386,76
    C 386,104 374,136 366,156
    C 384,180 422,206 458,226
    C 496,248 534,298 542,370
    C 550,455 540,580 498,695
    C 468,780 416,838 340,844
    C 264,838 212,780 182,695
    C 140,580 130,455 138,370
    C 146,298 184,248 222,226
    C 258,206 296,180 314,156
    C 310,141 306,131 292,126
    C 286,121 284,111 290,103
    C 282,96 280,86 286,79
    C 278,71 286,59 302,46
    C 316,35 328,32 340,32 Z
    """
    svg.append(f'<path d="{silhouette_path}" fill="#F8FAFC" stroke="#334155" stroke-width="1.8" stroke-linejoin="round" opacity="0.95" />')

    # 5. Left Design Column
    from app.core.line_fixations import calculate_chart_fixations
    des_fixations = chart_data.get("design_fixations") or calculate_chart_fixations(des_gates)
    pers_fixations = chart_data.get("personality_fixations") or calculate_chart_fixations(pers_gates)

    svg.append('<text x="72" y="46" fill="#0F172A" font-size="16" font-weight="700" text-anchor="middle">Design</text>')
    svg.append('<line x1="22" y1="56" x2="122" y2="56" stroke="#DC2626" stroke-width="2.5" stroke-linecap="round" />')

    y_start = 90
    row_gap = 52
    for idx, planet in enumerate(PLANET_ORDER):
        gate, line = des_gates.get(planet, (0, 0))
        symbol = PLANET_SYMBOLS.get(planet, "")
        y_pos = y_start + idx * row_gap
        arrow = des_fixations.get(planet, "")
        svg.append(f'<text x="34" y="{y_pos}" fill="#DC2626" font-size="20" font-weight="600" text-anchor="middle">{symbol}</text>')
        svg.append(f'<text x="76" y="{y_pos - 1}" fill="#DC2626" font-size="16.5" font-weight="600" text-anchor="middle">{gate}.{line}</text>')
        if arrow:
            svg.append(f'<text x="112" y="{y_pos - 2}" fill="#DC2626" font-size="13" font-weight="900" text-anchor="middle">{arrow}</text>')

    # 6. Right Personality Column
    svg.append('<text x="608" y="46" fill="#0F172A" font-size="16" font-weight="700" text-anchor="middle">Personality</text>')
    svg.append('<line x1="558" y1="56" x2="658" y2="56" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round" />')

    for idx, planet in enumerate(PLANET_ORDER):
        gate, line = pers_gates.get(planet, (0, 0))
        symbol = PLANET_SYMBOLS.get(planet, "")
        y_pos = y_start + idx * row_gap
        arrow = pers_fixations.get(planet, "")
        if arrow:
            svg.append(f'<text x="568" y="{y_pos - 2}" fill="#0F172A" font-size="13" font-weight="900" text-anchor="middle">{arrow}</text>')
        svg.append(f'<text x="604" y="{y_pos - 1}" fill="#0F172A" font-size="16.5" font-weight="600" text-anchor="middle">{gate}.{line}</text>')
        svg.append(f'<text x="646" y="{y_pos}" fill="#0F172A" font-size="20" font-weight="600" text-anchor="middle">{symbol}</text>')

    # 7. Variables (Top 4 Directional Arrows)
    svg.append(f'<text x="175" y="125" fill="#DC2626" font-size="28" font-weight="900" text-anchor="middle">{des_sun_arr}</text>')
    svg.append(f'<text x="175" y="240" fill="#DC2626" font-size="28" font-weight="900" text-anchor="middle">{des_node_arr}</text>')
    svg.append(f'<text x="505" y="125" fill="#0F172A" font-size="28" font-weight="900" text-anchor="middle">{pers_sun_arr}</text>')
    svg.append(f'<text x="505" y="240" fill="#0F172A" font-size="28" font-weight="900" text-anchor="middle">{pers_node_arr}</text>')

    # 8. Render All 36 Concentric & Sweeping Flow Channels
    from app.data.hd_topology import CHANNELS_DATA

    # Layer 8.1: Underlying Dual-Track White Guides
    for g1, g2, name, c1, c2 in CHANNELS_DATA:
        ch_key = (g1, g2)
        rev_key = (g2, g1)
        path_d = CHANNEL_PATHS.get(ch_key) or CHANNEL_PATHS.get(rev_key)
        if not path_d:
            p1 = CENTER_NODE_ANCHORS[c1]
            p2 = CENTER_NODE_ANCHORS[c2]
            path_d = f"M {p1[0]},{p1[1]} L {p2[0]},{p2[1]}"
        svg.append(f'<path d="{path_d}" stroke="#CBD5E1" stroke-width="8.5" stroke-linecap="round" fill="none" />')
        svg.append(f'<path d="{path_d}" stroke="#FFFFFF" stroke-width="5.5" stroke-linecap="round" fill="none" />')

    # Layer 8.2: Active Colored Channels
    for g1, g2, name, c1, c2 in CHANNELS_DATA:
        ch_key = (g1, g2)
        rev_key = (g2, g1)
        path_d = CHANNEL_PATHS.get(ch_key) or CHANNEL_PATHS.get(rev_key)
        if not path_d:
            p1 = CENTER_NODE_ANCHORS[c1]
            p2 = CENTER_NODE_ANCHORS[c2]
            path_d = f"M {p1[0]},{p1[1]} L {p2[0]},{p2[1]}"

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
            svg.append(f'<path d="{half_1}" stroke="#DC2626" stroke-width="7.5" stroke-linecap="butt" fill="none" />')
            svg.append(f'<path d="{half_1}" stroke="#18181B" stroke-width="7.5" stroke-dasharray="6 6" stroke-linecap="butt" fill="none" />')
        elif is_des_1:
            svg.append(f'<path d="{half_1}" stroke="#DC2626" stroke-width="7.5" stroke-linecap="butt" fill="none" />')
        elif is_pers_1:
            svg.append(f'<path d="{half_1}" stroke="#18181B" stroke-width="7.5" stroke-linecap="butt" fill="none" />')

        # Gate 2 activation
        is_pers_2 = g2 in pers_gate_set
        is_des_2 = g2 in des_gate_set
        if is_pers_2 and is_des_2:
            svg.append(f'<path d="{half_2}" stroke="#DC2626" stroke-width="7.5" stroke-linecap="butt" fill="none" />')
            svg.append(f'<path d="{half_2}" stroke="#18181B" stroke-width="7.5" stroke-dasharray="6 6" stroke-linecap="butt" fill="none" />')
        elif is_des_2:
            svg.append(f'<path d="{half_2}" stroke="#DC2626" stroke-width="7.5" stroke-linecap="butt" fill="none" />')
        elif is_pers_2:
            svg.append(f'<path d="{half_2}" stroke="#18181B" stroke-width="7.5" stroke-linecap="butt" fill="none" />')

    # 9. Render The 9 Harmonized Energy Centers
    for c_name, c_info in CENTERS_DATA.items():
        is_def = c_name in defined_centers
        fill_color = c_info["defined_color"] if is_def else c_info["undefined_color"]
        stroke_color = c_info["defined_stroke"] if is_def else c_info["undefined_stroke"]

        if c_info["type"] == "rect":
            rx, ry, rw, rh, rradius = c_info["rect"]
            svg.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="{rradius}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="2.0" />')
        elif c_info["type"] == "polygon":
            pts = c_info["points"]
            svg.append(f'<polygon points="{pts}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="2.0" stroke-linejoin="round" />')

    # 10. Gate Numbers & Active Badges with Maximum Legibility
    for g_num, (gx, gy) in GATE_POS.items():
        is_active = g_num in active_gates
        parent_center = GATE_CENTER_MAP.get(g_num, "")
        is_parent_defined = parent_center in defined_centers

        if is_active:
            if is_parent_defined:
                # Active on Defined Center: Crisp Solid White Circle + Bold Black Number
                svg.append(f'<circle cx="{gx}" cy="{gy}" r="8.5" fill="#FFFFFF" stroke="#000000" stroke-width="0.5" />')
                svg.append(f'<text x="{gx}" y="{gy + 3.8}" fill="#000000" font-size="11" font-weight="900" text-anchor="middle">{g_num}</text>')
            else:
                # Active on Light Undefined Center: Ultra-Bold Black Number
                svg.append(f'<text x="{gx}" y="{gy + 3.8}" fill="#000000" font-size="11.5" font-weight="900" text-anchor="middle">{g_num}</text>')
        else:
            if is_parent_defined:
                # Inactive on Dark Center: Crisp High-Contrast White Text
                svg.append(f'<text x="{gx}" y="{gy + 3.5}" fill="#FFFFFF" opacity="0.9" font-size="10" font-weight="700" text-anchor="middle">{g_num}</text>')
            else:
                # Inactive on Undefined White Center: Soft Slate Grey Text
                svg.append(f'<text x="{gx}" y="{gy + 3.5}" fill="#64748B" font-size="10" font-weight="600" text-anchor="middle">{g_num}</text>')

    svg.append('</svg>')
    return "".join(svg)
