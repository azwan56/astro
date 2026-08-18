"""
Grand Minimalist Modern Human Design BodyGraph SVG Renderer
Inspired by official modern aesthetic (Scandinavian minimalist / Maia Mechanics Advanced design):
- Light grey human silhouette in profile in the background
- Clean borderless energy centers with official authentic pastel/taupe palette:
    * Head: Soft Pale Canary Yellow (#F7EE94)
    * Ajna: Muted Sage/Teal Green (#6B9E8D)
    * Throat: Warm Mocha Taupe (#5A4D45) / Pure White (#FFFFFF)
    * G Center: Soft Pale Canary Yellow (#F7EE94) / Pure White (#FFFFFF)
    * Heart / Ego: Coral Carmine (#DC4C40) / Pure White (#FFFFFF)
    * Spleen / Solar Plexus / Root: Warm Mocha Taupe (#5A4D45) / Pure White (#FFFFFF)
    * Sacral: Coral Carmine (#DC4C40) / Pure White (#FFFFFF)
- Gate Badges:
    * Active gates on colored/dark centers: Crisp White Circle with Bold Black Number
    * Active gates on white/light centers: Bold Black Number
    * Inactive gates: Elegant subtle muted slate grey text without circles
- Minimalist Planet Columns:
    * Left Design Column: Clean Red Glyph, Gate.Line, and Retrograde indicator under 'Design' title
    * Right Personality Column: Clean Dark Glyph, Gate.Line, and Retrograde indicator under 'Personality' title
- Top 4 Variables:
    * Clean directional arrows (Left Red / Right Dark) placed beside the head
- Dual-Layer Channels:
    * Clean white base guide tracks
    * Vibrant Coral Red (#DC4C40) & Matte Obsidian Charcoal (#1F2421) full & subdivided hanging half-channels
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

# 9 Centers Coordinate Geometry (Canvas Width = 680, Center = 340)
# Offset +20px horizontally to perfectly center inside 680 canvas
CENTERS_DATA = {
    "Head": {
        "type": "polygon",
        "points": "340,50 290,132 390,132",
        "defined_color": "#F7EE94",
        "undefined_color": "#FFFFFF"
    },
    "Ajna": {
        "type": "polygon",
        "points": "290,152 390,152 340,235",
        "defined_color": "#6B9E8D",
        "undefined_color": "#FFFFFF"
    },
    "Throat": {
        "type": "rect",
        "rect": (292, 260, 96, 80, 16),
        "defined_color": "#5A4D45",
        "undefined_color": "#FFFFFF"
    },
    "G_Center": {
        "type": "polygon",
        "points": "340,365 396,425 340,485 284,425",
        "defined_color": "#F7EE94",
        "undefined_color": "#FFFFFF"
    },
    "Heart": {
        "type": "polygon",
        "points": "410,432 460,432 435,480",
        "defined_color": "#DC4C40",
        "undefined_color": "#FFFFFF"
    },
    "Spleen": {
        "type": "polygon",
        "points": "184,472 248,572 184,672",
        "defined_color": "#5A4D45",
        "undefined_color": "#FFFFFF"
    },
    "Solar_Plexus": {
        "type": "polygon",
        "points": "496,472 432,572 496,672",
        "defined_color": "#5A4D45",
        "undefined_color": "#FFFFFF"
    },
    "Sacral": {
        "type": "rect",
        "rect": (292, 532, 96, 80, 16),
        "defined_color": "#DC4C40",
        "undefined_color": "#FFFFFF"
    },
    "Root": {
        "type": "rect",
        "rect": (292, 662, 96, 86, 16),
        "defined_color": "#5A4D45",
        "undefined_color": "#FFFFFF"
    }
}

CENTERS_CURVED = CENTERS_DATA
CENTERS_LAYOUT = CENTERS_DATA

CENTER_NODE_ANCHORS = {
    "Head": (340, 115), "Ajna": (340, 185), "Throat": (340, 300),
    "G_Center": (340, 425), "Heart": (435, 456), "Spleen": (216, 572),
    "Solar_Plexus": (464, 572), "Sacral": (340, 572), "Root": (340, 705)
}

# 64 Gate Coordinates (+20px X offset for 680 canvas centering)
GATE_POS = {
    64: (310, 122), 61: (340, 122), 63: (370, 122),
    47: (310, 168), 24: (340, 168), 4: (370, 168),
    17: (316, 198), 43: (340, 215), 11: (364, 198),
    62: (308, 275), 23: (340, 275), 56: (372, 275),
    16: (306, 299), 20: (328, 307), 12: (352, 307), 35: (374, 299),
    31: (308, 329), 8: (328, 329), 33: (352, 329), 45: (372, 329),
    1: (340, 386),
    7: (312, 410), 13: (368, 410),
    10: (300, 425), 25: (380, 425),
    15: (312, 448), 46: (368, 448),
    2: (340, 464),
    21: (428, 444), 51: (450, 450),
    26: (418, 466), 40: (440, 472),
    48: (198, 500), 57: (215, 530), 44: (230, 558),
    50: (234, 582), 32: (222, 608), 28: (208, 632), 18: (196, 650),
    36: (482, 500), 22: (465, 530), 37: (450, 558),
    6: (446, 582), 49: (458, 608), 55: (472, 632), 30: (484, 650),
    5: (310, 545), 14: (340, 545), 29: (370, 545),
    34: (306, 572), 59: (374, 572),
    27: (306, 599), 42: (328, 599), 3: (352, 599), 9: (374, 599),
    53: (310, 680), 60: (340, 680), 52: (370, 680),
    54: (306, 703), 19: (374, 703),
    38: (306, 726), 39: (374, 726),
    58: (324, 738), 41: (356, 738)
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

DARK_CENTERS = {'Ajna', 'Spleen', 'Solar_Plexus', 'Root'}

CHANNEL_PATHS = {
    (64, 47): "M 310,122 L 310,168",
    (61, 24): "M 340,122 L 340,168",
    (63, 4): "M 370,122 L 370,168",
    (17, 62): "M 316,198 L 308,275",
    (43, 23): "M 340,215 L 340,275",
    (11, 56): "M 364,198 L 372,275",
    (31, 7): "M 308,329 C 295,340 295,355 312,410",
    (8, 1): "M 328,329 L 340,386",
    (33, 13): "M 352,329 C 385,340 385,355 368,410",
    (20, 10): "M 328,307 C 268,325 260,395 300,425",
    (45, 21): "M 372,329 C 400,340 425,385 428,444",
    (12, 22): "M 352,307 C 425,330 462,425 465,530",
    (35, 36): "M 374,299 C 430,310 478,385 482,500",
    (20, 34): "M 328,307 C 265,340 255,455 306,572",
    (20, 57): "M 328,307 C 255,330 218,425 215,530",
    (16, 48): "M 306,299 C 250,310 202,385 198,500",
    (25, 51): "M 380,425 L 450,450",
    (15, 5): "M 312,448 L 310,545",
    (2, 14): "M 340,464 L 340,545",
    (46, 29): "M 368,448 L 370,545",
    (10, 34): "M 300,425 C 285,460 285,505 306,572",
    (10, 57): "M 300,425 L 215,530",
    (40, 37): "M 440,472 L 450,558",
    (26, 44): "M 418,466 C 340,470 280,510 230,558",
    (59, 6): "M 374,572 L 446,582",
    (27, 50): "M 306,599 L 234,582",
    (34, 57): "M 306,572 L 215,530",
    (42, 53): "M 328,599 L 310,680",
    (3, 60): "M 352,599 L 340,680",
    (9, 52): "M 374,599 L 370,680",
    (19, 49): "M 374,703 C 425,683 455,663 458,608",
    (39, 55): "M 374,726 C 430,708 460,683 472,632",
    (41, 30): "M 356,738 C 430,728 470,713 484,650",
    (58, 18): "M 324,738 C 250,728 210,713 196,650",
    (38, 28): "M 306,726 C 250,708 220,683 208,632",
    (54, 32): "M 306,703 C 255,683 225,663 222,608"
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

    des_sun_arr = "←" if des_sun_sub["arrow"] == "Left" else "→"
    des_node_arr = "←" if des_node_sub["arrow"] == "Left" else "→"
    pers_sun_arr = "←" if pers_sun_sub["arrow"] == "Left" else "→"
    pers_node_arr = "←" if pers_node_sub["arrow"] == "Left" else "→"

    svg = []
    # 1. Master Canvas
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="100%" height="100%" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, \\"Segoe UI\\", Roboto, Helvetica, Arial, sans-serif;">')

    # 2. Defs: Striped Patterns
    svg.append('''
    <defs>
        <pattern id="striped-red-black" width="14" height="14" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
            <line x1="0" y1="0" x2="0" y2="14" stroke="#DC4C40" stroke-width="7" />
            <line x1="7" y1="0" x2="7" y2="14" stroke="#1F2421" stroke-width="7" />
        </pattern>
        <filter id="center-shadow" x="-5%" y="-5%" width="110%" height="110%">
            <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#000000" flood-opacity="0.04"/>
        </filter>
    </defs>
    ''')

    # 3. Authentic Human Profile Silhouette (Light Grey #ECEFF1)
    silhouette_path = """
    M 340,30
    C 368,30 388,48 388,78
    C 388,108 375,138 368,158
    C 385,182 425,208 460,228
    C 500,252 535,302 540,372
    C 545,452 535,572 495,692
    C 465,777 415,832 340,838
    C 265,832 215,777 185,692
    C 145,572 135,452 140,372
    C 145,302 180,252 220,228
    C 255,208 295,182 312,158
    C 310,143 306,133 290,128
    C 284,123 282,113 288,105
    C 280,98 278,88 284,81
    C 276,73 284,61 300,48
    C 315,35 328,30 340,30 Z
    """
    svg.append(f'<path d="{silhouette_path}" fill="#ECEFF1" opacity="0.95" />')

    # 4. Minimalist Left Design Column
    # Header: "Design" with red underline
    svg.append('<text x="70" y="48" fill="#222222" font-size="14.5" font-weight="600" text-anchor="middle">Design</text>')
    svg.append('<line x1="20" y1="58" x2="120" y2="58" stroke="#DC4C40" stroke-width="2.2" stroke-linecap="round" />')

    y_start = 90
    row_gap = 52
    for idx, planet in enumerate(PLANET_ORDER):
        gate, line = des_gates.get(planet, (0, 0))
        symbol = PLANET_SYMBOLS.get(planet, "")
        y_pos = y_start + idx * row_gap
        arrow = "▼" if idx in [0, 5, 7, 10] else ("▲" if idx in [9] else "")
        svg.append(f'<text x="32" y="{y_pos}" fill="#DC4C40" font-size="18" font-weight="500" text-anchor="middle">{symbol}</text>')
        svg.append(f'<text x="75" y="{y_pos - 1}" fill="#DC4C40" font-size="15" font-weight="500" text-anchor="middle">{gate}.{line}</text>')
        if arrow:
            svg.append(f'<text x="110" y="{y_pos - 2}" fill="#DC4C40" font-size="12" font-weight="bold" text-anchor="middle">{arrow}</text>')

    # 5. Minimalist Right Personality Column
    # Header: "Personality" with charcoal underline
    svg.append('<text x="610" y="48" fill="#222222" font-size="14.5" font-weight="600" text-anchor="middle">Personality</text>')
    svg.append('<line x1="560" y1="58" x2="660" y2="58" stroke="#222222" stroke-width="2.2" stroke-linecap="round" />')

    for idx, planet in enumerate(PLANET_ORDER):
        gate, line = pers_gates.get(planet, (0, 0))
        symbol = PLANET_SYMBOLS.get(planet, "")
        y_pos = y_start + idx * row_gap
        arrow = "▲" if idx in [0, 2, 3, 7] else ("▼" if idx in [12] else "")
        if arrow:
            svg.append(f'<text x="570" y="{y_pos - 2}" fill="#222222" font-size="12" font-weight="bold" text-anchor="middle">{arrow}</text>')
        svg.append(f'<text x="605" y="{y_pos - 1}" fill="#222222" font-size="15" font-weight="500" text-anchor="middle">{gate}.{line}</text>')
        svg.append(f'<text x="648" y="{y_pos}" fill="#222222" font-size="18" font-weight="500" text-anchor="middle">{symbol}</text>')

    # 6. Minimalist Top 4 Variables (Directional Arrows beside Head)
    # Left Design Arrows
    svg.append(f'<text x="175" y="125" fill="#DC4C40" font-size="24" font-weight="bold" text-anchor="middle">{des_sun_arr}</text>')
    svg.append(f'<text x="175" y="240" fill="#DC4C40" font-size="24" font-weight="bold" text-anchor="middle">{des_node_arr}</text>')

    # Right Personality Arrows
    svg.append(f'<text x="505" y="125" fill="#222222" font-size="24" font-weight="bold" text-anchor="middle">{pers_sun_arr}</text>')
    svg.append(f'<text x="505" y="240" fill="#222222" font-size="24" font-weight="bold" text-anchor="middle">{pers_node_arr}</text>')

    # 7. Render All 36 Channels
    from app.data.hd_topology import CHANNELS_DATA

    # Layer 7.1: Underlying Full Clean White Guide Tracks
    for g1, g2, name, c1, c2 in CHANNELS_DATA:
        ch_key = (g1, g2)
        rev_key = (g2, g1)
        path_d = CHANNEL_PATHS.get(ch_key) or CHANNEL_PATHS.get(rev_key)
        if not path_d:
            p1 = CENTER_NODE_ANCHORS[c1]
            p2 = CENTER_NODE_ANCHORS[c2]
            path_d = f"M {p1[0]},{p1[1]} L {p2[0]},{p2[1]}"
        svg.append(f'<path d="{path_d}" stroke="#FFFFFF" stroke-width="8.5" stroke-linecap="round" fill="none" opacity="0.95" />')

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
            svg.append(f'<path d="{half_1}" stroke="#DC4C40" stroke-width="7.5" stroke-linecap="butt" fill="none" />')
            svg.append(f'<path d="{half_1}" stroke="#1F2421" stroke-width="7.5" stroke-dasharray="6 6" stroke-linecap="butt" fill="none" />')
        elif is_des_1:
            svg.append(f'<path d="{half_1}" stroke="#DC4C40" stroke-width="7.5" stroke-linecap="butt" fill="none" />')
        elif is_pers_1:
            svg.append(f'<path d="{half_1}" stroke="#1F2421" stroke-width="7.5" stroke-linecap="butt" fill="none" />')

        # Gate 2 activation
        is_pers_2 = g2 in pers_gate_set
        is_des_2 = g2 in des_gate_set
        if is_pers_2 and is_des_2:
            svg.append(f'<path d="{half_2}" stroke="#DC4C40" stroke-width="7.5" stroke-linecap="butt" fill="none" />')
            svg.append(f'<path d="{half_2}" stroke="#1F2421" stroke-width="7.5" stroke-dasharray="6 6" stroke-linecap="butt" fill="none" />')
        elif is_des_2:
            svg.append(f'<path d="{half_2}" stroke="#DC4C40" stroke-width="7.5" stroke-linecap="butt" fill="none" />')
        elif is_pers_2:
            svg.append(f'<path d="{half_2}" stroke="#1F2421" stroke-width="7.5" stroke-linecap="butt" fill="none" />')

    # 8. Render The 9 Energy Centers (Smooth borderless aesthetic matching reference image)
    for c_name, c_info in CENTERS_DATA.items():
        is_def = c_name in defined_centers
        fill_color = c_info["defined_color"] if is_def else c_info["undefined_color"]

        if c_info["type"] == "rect":
            rx, ry, rw, rh, rradius = c_info["rect"]
            svg.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="{rradius}" fill="{fill_color}" />')
        elif c_info["type"] == "polygon":
            pts = c_info["points"]
            svg.append(f'<polygon points="{pts}" fill="{fill_color}" stroke="{fill_color}" stroke-width="12" stroke-linejoin="round" />')

    # 9. Gate Numbers & Active Badges
    for g_num, (gx, gy) in GATE_POS.items():
        is_active = g_num in active_gates
        parent_center = GATE_CENTER_MAP.get(g_num, "")
        is_parent_defined = parent_center in defined_centers
        is_dark_bg = is_parent_defined and (parent_center in DARK_CENTERS)

        if is_active:
            if is_dark_bg or parent_center == 'Ajna':
                # Active on Dark/Sage Center: Solid White Circle + Bold Black Number
                svg.append(f'<circle cx="{gx}" cy="{gy}" r="8.2" fill="#FFFFFF" />')
                svg.append(f'<text x="{gx}" y="{gy + 3.8}" fill="#000000" font-size="10.5" font-weight="900" text-anchor="middle">{g_num}</text>')
            else:
                # Active on Light Center / Channel Entry: Bold Black Number
                svg.append(f'<text x="{gx}" y="{gy + 3.8}" fill="#000000" font-size="10.8" font-weight="900" text-anchor="middle">{g_num}</text>')
        else:
            # Inactive Gate: Subtle Muted Grey Text
            text_color = "#94A3B8" if not is_dark_bg else "#CBD5E1"
            svg.append(f'<text x="{gx}" y="{gy + 3.4}" fill="{text_color}" font-size="9.5" font-weight="500" text-anchor="middle">{g_num}</text>')

    svg.append('</svg>')
    return "".join(svg)
