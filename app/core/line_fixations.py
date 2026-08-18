"""
Rave I Ching 384-Line Planetary Fixation Engine (Exaltation ▲ & Detriment ▼)
Standard Human Design calculations matching official Jovian Archive / MMI.

Each of the 64 Gates and 6 Lines (384 lines total) has specific planetary fixations:
- Exaltation (▲): The planet triggers the highest/most harmonious expression of this line.
- Detriment (▼): The planet triggers the challenging/growth-oriented expression of this line.
- Juxtaposition (*): Rare binary dual resonance.
"""

from typing import Dict, List, Tuple

# Comprehensive Rave I Ching 384 Lines Planetary Fixations Database
# Format: (gate, line): {"exalted": [planets...], "detriment": [planets...]}
RAVE_LINE_FIXATIONS: Dict[Tuple[int, int], Dict[str, List[str]]] = {
    # Gate 1
    (1, 1): {"exalted": ["Moon"], "detriment": ["Uranus"]},
    (1, 2): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (1, 3): {"exalted": ["Mars"], "detriment": ["Earth"]},
    (1, 4): {"exalted": ["Earth"], "detriment": ["Jupiter"]},
    (1, 5): {"exalted": ["Mars"], "detriment": ["Uranus"]},
    (1, 6): {"exalted": ["Earth"], "detriment": ["Pluto"]},

    # Gate 2
    (2, 1): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (2, 2): {"exalted": ["Saturn"], "detriment": ["Mars"]},
    (2, 3): {"exalted": ["Jupiter"], "detriment": ["Uranus"]},
    (2, 4): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (2, 5): {"exalted": ["Mercury"], "detriment": ["Earth"]},
    (2, 6): {"exalted": ["Mercury"], "detriment": ["Saturn"]},

    # Gate 3
    (3, 1): {"exalted": ["Earth"], "detriment": ["Mercury"]},
    (3, 2): {"exalted": ["Mars"], "detriment": ["Uranus"]},
    (3, 3): {"exalted": ["Venus"], "detriment": ["Pluto"]},
    (3, 4): {"exalted": ["Neptune"], "detriment": ["Mars"]},
    (3, 5): {"exalted": ["Mars"], "detriment": ["Earth"]},
    (3, 6): {"exalted": ["Sun"], "detriment": ["Pluto"]},

    # Gate 4
    (4, 1): {"exalted": ["Moon"], "detriment": ["Earth"]},
    (4, 2): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (4, 3): {"exalted": ["Venus"], "detriment": ["Pluto"]},
    (4, 4): {"exalted": ["Sun"], "detriment": ["Saturn"]},
    (4, 5): {"exalted": ["Jupiter"], "detriment": ["Pluto"]},
    (4, 6): {"exalted": ["Mercury"], "detriment": ["Mars"]},

    # Gate 5
    (5, 1): {"exalted": ["Mars"], "detriment": ["Venus"]},
    (5, 2): {"exalted": ["Venus"], "detriment": ["Pluto"]},
    (5, 3): {"exalted": ["Neptune"], "detriment": ["Moon"]},
    (5, 4): {"exalted": ["Uranus"], "detriment": ["Sun"]},
    (5, 5): {"exalted": ["Venus"], "detriment": ["Pluto"]},
    (5, 6): {"exalted": ["Neptune"], "detriment": ["Mars"]},

    # Gate 6
    (6, 1): {"exalted": ["Pluto"], "detriment": ["Mercury"]},
    (6, 2): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (6, 3): {"exalted": ["Neptune"], "detriment": ["Pluto"]},
    (6, 4): {"exalted": ["Sun"], "detriment": ["Pluto"]},
    (6, 5): {"exalted": ["Venus"], "detriment": ["Moon"]},
    (6, 6): {"exalted": ["Mars"], "detriment": ["Mercury"]},

    # Gate 7
    (7, 1): {"exalted": ["Venus"], "detriment": ["Mercury"]},
    (7, 2): {"exalted": ["Neptune"], "detriment": ["Mercury"]},
    (7, 3): {"exalted": ["Moon"], "detriment": ["Mercury"]},
    (7, 4): {"exalted": ["Sun"], "detriment": ["Uranus"]},
    (7, 5): {"exalted": ["Venus"], "detriment": ["Neptune"]},
    (7, 6): {"exalted": ["Mercury"], "detriment": ["Pluto"]},

    # Gate 8
    (8, 1): {"exalted": ["Neptune"], "detriment": ["Mars"]},
    (8, 2): {"exalted": ["Sun"], "detriment": ["Earth"]},
    (8, 3): {"exalted": ["Moon"], "detriment": ["Pluto"]},
    (8, 4): {"exalted": ["Jupiter"], "detriment": ["Mercury"]},
    (8, 5): {"exalted": ["Jupiter"], "detriment": ["Sun"]},
    (8, 6): {"exalted": ["Venus"], "detriment": ["Pluto"]},

    # Gate 9
    (9, 1): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (9, 2): {"exalted": ["Pluto"], "detriment": ["Jupiter"]},
    (9, 3): {"exalted": ["Earth"], "detriment": ["Sun"]},
    (9, 4): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (9, 5): {"exalted": ["Jupiter"], "detriment": ["Earth"]},
    (9, 6): {"exalted": ["Sun", "Moon"], "detriment": ["Pluto"]},

    # Gate 10
    (10, 1): {"exalted": ["Sun"], "detriment": ["Moon"]},
    (10, 2): {"exalted": ["Mercury"], "detriment": ["Mars"]},
    (10, 3): {"exalted": ["Earth"], "detriment": ["Moon"]},
    (10, 4): {"exalted": ["Uranus"], "detriment": ["Mercury"]},
    (10, 5): {"exalted": ["Jupiter"], "detriment": ["Saturn"]},
    (10, 6): {"exalted": ["Pluto"], "detriment": ["Saturn"]},

    # Gate 11
    (11, 1): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (11, 2): {"exalted": ["Neptune"], "detriment": ["Mars"]},
    (11, 3): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (11, 4): {"exalted": ["Moon"], "detriment": ["Mercury"]},
    (11, 5): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (11, 6): {"exalted": ["Sun"], "detriment": ["Earth"]},

    # Gate 12
    (12, 1): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (12, 2): {"exalted": ["Saturn"], "detriment": ["Mercury"]},
    (12, 3): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (12, 4): {"exalted": ["Earth"], "detriment": ["Mercury"]},
    (12, 5): {"exalted": ["Sun"], "detriment": ["Mars"]},
    (12, 6): {"exalted": ["Sun"], "detriment": ["Earth"]},

    # Gate 13
    (13, 1): {"exalted": ["Venus"], "detriment": ["Moon"]},
    (13, 2): {"exalted": ["Moon"], "detriment": ["Sun"]},
    (13, 3): {"exalted": ["Earth"], "detriment": ["Venus"]},
    (13, 4): {"exalted": ["Pluto"], "detriment": ["Venus"]},
    (13, 5): {"exalted": ["Neptune"], "detriment": ["Jupiter"]},
    (13, 6): {"exalted": ["Mars"], "detriment": ["Mercury"]},

    # Gate 14
    (14, 1): {"exalted": ["Mercury"], "detriment": ["Jupiter"]},
    (14, 2): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (14, 3): {"exalted": ["Earth"], "detriment": ["Mars"]},
    (14, 4): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (14, 5): {"exalted": ["Sun"], "detriment": ["Venus"]},
    (14, 6): {"exalted": ["Sun"], "detriment": ["Earth"]},

    # Gate 15
    (15, 1): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (15, 2): {"exalted": ["Sun"], "detriment": ["Earth"]},
    (15, 3): {"exalted": ["Earth"], "detriment": ["Mars"]},
    (15, 4): {"exalted": ["Jupiter"], "detriment": ["Pluto"]},
    (15, 5): {"exalted": ["Jupiter"], "detriment": ["Pluto"]},
    (15, 6): {"exalted": ["Pluto"], "detriment": ["Venus"]},

    # Gate 16
    (16, 1): {"exalted": ["Earth"], "detriment": ["Mercury"]},
    (16, 2): {"exalted": ["Sun"], "detriment": ["Mercury"]},
    (16, 3): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (16, 4): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (16, 5): {"exalted": ["Pluto"], "detriment": ["Moon"]},
    (16, 6): {"exalted": ["Neptune"], "detriment": ["Jupiter"]},

    # Gate 17
    (17, 1): {"exalted": ["Mars"], "detriment": ["Venus"]},
    (17, 2): {"exalted": ["Sun"], "detriment": ["Moon"]},
    (17, 3): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (17, 4): {"exalted": ["Pluto"], "detriment": ["Jupiter"]},
    (17, 5): {"exalted": ["Sun"], "detriment": ["Uranus"]},
    (17, 6): {"exalted": ["Moon"], "detriment": ["Jupiter"]},

    # Gate 18
    (18, 1): {"exalted": ["Earth"], "detriment": ["Moon"]},
    (18, 2): {"exalted": ["Pluto"], "detriment": ["Moon"]},
    (18, 3): {"exalted": ["Saturn"], "detriment": ["Mars"]},
    (18, 4): {"exalted": ["Jupiter"], "detriment": ["Sun"]},
    (18, 5): {"exalted": ["Saturn"], "detriment": ["Uranus"]},
    (18, 6): {"exalted": ["Moon"], "detriment": ["Mars"]},

    # Gate 19
    (19, 1): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (19, 2): {"exalted": ["Jupiter"], "detriment": ["Mercury"]},
    (19, 3): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (19, 4): {"exalted": ["Mars"], "detriment": ["Venus"]},
    (19, 5): {"exalted": ["Earth"], "detriment": ["Jupiter"]},
    (19, 6): {"exalted": ["Sun"], "detriment": ["Jupiter"]},

    # Gate 20
    (20, 1): {"exalted": ["Venus"], "detriment": ["Moon"]},
    (20, 2): {"exalted": ["Venus"], "detriment": ["Moon"]},
    (20, 3): {"exalted": ["South_Node"], "detriment": ["Sun"]},
    (20, 4): {"exalted": ["Jupiter"], "detriment": ["Mercury"]},
    (20, 5): {"exalted": ["Saturn"], "detriment": ["Uranus"]},
    (20, 6): {"exalted": ["Venus"], "detriment": ["Mercury"]},

    # Gate 21
    (21, 1): {"exalted": ["Mars"], "detriment": ["Moon"]},
    (21, 2): {"exalted": ["Mars"], "detriment": ["Jupiter"]},
    (21, 3): {"exalted": ["Mars"], "detriment": ["Jupiter"]},
    (21, 4): {"exalted": ["Jupiter"], "detriment": ["Pluto"]},
    (21, 5): {"exalted": ["Jupiter"], "detriment": ["Venus"]},
    (21, 6): {"exalted": ["Pluto"], "detriment": ["Venus"]},

    # Gate 22
    (22, 1): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (22, 2): {"exalted": ["Sun"], "detriment": ["Jupiter"]},
    (22, 3): {"exalted": ["Saturn"], "detriment": ["Mars"]},
    (22, 4): {"exalted": ["Neptune"], "detriment": ["Mars"]},
    (22, 5): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (22, 6): {"exalted": ["Sun"], "detriment": ["Mars"]},

    # Gate 23
    (23, 1): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (23, 2): {"exalted": ["Jupiter"], "detriment": ["Moon"]},
    (23, 3): {"exalted": ["Sun"], "detriment": ["Pluto"]},
    (23, 4): {"exalted": ["Sun"], "detriment": ["Earth"]},
    (23, 5): {"exalted": ["Jupiter"], "detriment": ["Moon"]},
    (23, 6): {"exalted": ["Mars"], "detriment": ["Jupiter"]},

    # Gate 24
    (24, 1): {"exalted": ["Sun"], "detriment": ["Pluto"]},
    (24, 2): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (24, 3): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (24, 4): {"exalted": ["Saturn"], "detriment": ["Mars"]},
    (24, 5): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (24, 6): {"exalted": ["Jupiter"], "detriment": ["Pluto"]},

    # Gate 25
    (25, 1): {"exalted": ["Neptune"], "detriment": ["Mars"]},
    (25, 2): {"exalted": ["Mercury"], "detriment": ["Mars"]},
    (25, 3): {"exalted": ["Mercury"], "detriment": ["Mars"]},
    (25, 4): {"exalted": ["Venus"], "detriment": ["Jupiter"]},
    (25, 5): {"exalted": ["Venus"], "detriment": ["Jupiter"]},
    (25, 6): {"exalted": ["Earth"], "detriment": ["Pluto"]},

    # Gate 26
    (26, 1): {"exalted": ["Neptune"], "detriment": ["Mars"]},
    (26, 2): {"exalted": ["Sun"], "detriment": ["Mars"]},
    (26, 3): {"exalted": ["Sun"], "detriment": ["Mars"]},
    (26, 4): {"exalted": ["Saturn"], "detriment": ["Mars"]},
    (26, 5): {"exalted": ["Jupiter"], "detriment": ["Moon"]},
    (26, 6): {"exalted": ["Sun"], "detriment": ["Moon"]},

    # Gate 27
    (27, 1): {"exalted": ["Earth"], "detriment": ["Moon"]},
    (27, 2): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (27, 3): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (27, 4): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (27, 5): {"exalted": ["Jupiter"], "detriment": ["Saturn"]},
    (27, 6): {"exalted": ["Moon"], "detriment": ["Pluto"]},

    # Gate 28
    (28, 1): {"exalted": ["Mars"], "detriment": ["Venus"]},
    (28, 2): {"exalted": ["Sun"], "detriment": ["Pluto"]},
    (28, 3): {"exalted": ["Saturn"], "detriment": ["Jupiter"]},
    (28, 4): {"exalted": ["Jupiter"], "detriment": ["Pluto"]},
    (28, 5): {"exalted": ["Pluto"], "detriment": ["Sun"]},
    (28, 6): {"exalted": ["Saturn", "North_Node"], "detriment": ["Pluto"]},

    # Gate 29
    (29, 1): {"exalted": ["Mars"], "detriment": ["Sun"]},
    (29, 2): {"exalted": ["Sun"], "detriment": ["Venus"]},
    (29, 3): {"exalted": ["Mars"], "detriment": ["Jupiter"]},
    (29, 4): {"exalted": ["Saturn"], "detriment": ["Mars"]},
    (29, 5): {"exalted": ["Sun"], "detriment": ["Earth"]},
    (29, 6): {"exalted": ["Mars"], "detriment": ["Jupiter"]},

    # Gate 30
    (30, 1): {"exalted": ["Sun"], "detriment": ["Jupiter"]},
    (30, 2): {"exalted": ["Sun"], "detriment": ["Mars"]},
    (30, 3): {"exalted": ["Pluto"], "detriment": ["Jupiter"]},
    (30, 4): {"exalted": ["Pluto"], "detriment": ["Jupiter"]},
    (30, 5): {"exalted": ["Moon"], "detriment": ["Jupiter"]},
    (30, 6): {"exalted": ["Mars"], "detriment": ["Moon"]},

    # Gate 31
    (31, 1): {"exalted": ["Sun"], "detriment": ["Earth"]},
    (31, 2): {"exalted": ["Jupiter"], "detriment": ["Mercury"]},
    (31, 3): {"exalted": ["Sun"], "detriment": ["Jupiter"]},
    (31, 4): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (31, 5): {"exalted": ["Pluto"], "detriment": ["Moon"]},
    (31, 6): {"exalted": ["Moon"], "detriment": ["Sun"]},

    # Gate 32
    (32, 1): {"exalted": ["Sun"], "detriment": ["Moon"]},
    (32, 2): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (32, 3): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (32, 4): {"exalted": ["Jupiter"], "detriment": ["Saturn"]},
    (32, 5): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (32, 6): {"exalted": ["Pluto"], "detriment": ["Mars"]},

    # Gate 33
    (33, 1): {"exalted": ["Sun"], "detriment": ["Mars"]},
    (33, 2): {"exalted": ["Jupiter"], "detriment": ["Neptune"]},
    (33, 3): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (33, 4): {"exalted": ["Pluto"], "detriment": ["Sun"]},
    (33, 5): {"exalted": ["Jupiter"], "detriment": ["Pluto"]},
    (33, 6): {"exalted": ["Sun"], "detriment": ["Jupiter"]},

    # Gate 34
    (34, 1): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (34, 2): {"exalted": ["Mars"], "detriment": ["Venus"]},
    (34, 3): {"exalted": ["Earth"], "detriment": ["Mars"]},
    (34, 4): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (34, 5): {"exalted": ["Mars"], "detriment": ["Moon"]},
    (34, 6): {"exalted": ["Earth"], "detriment": ["Pluto"]},

    # Gate 35
    (35, 1): {"exalted": ["Venus"], "detriment": ["Mercury"]},
    (35, 2): {"exalted": ["Venus"], "detriment": ["Moon"]},
    (35, 3): {"exalted": ["Sun"], "detriment": ["Mars"]},
    (35, 4): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (35, 5): {"exalted": ["Mercury"], "detriment": ["Jupiter"]},
    (35, 6): {"exalted": ["Sun"], "detriment": ["Pluto"]},

    # Gate 36
    (36, 1): {"exalted": ["Pluto"], "detriment": ["Jupiter"]},
    (36, 2): {"exalted": ["Moon"], "detriment": ["Neptune"]},
    (36, 3): {"exalted": ["Pluto"], "detriment": ["Jupiter"]},
    (36, 4): {"exalted": ["Pluto"], "detriment": ["Moon"]},
    (36, 5): {"exalted": ["Sun"], "detriment": ["Moon"]},
    (36, 6): {"exalted": ["Jupiter"], "detriment": ["Saturn"]},

    # Gate 37
    (37, 1): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (37, 2): {"exalted": ["Venus"], "detriment": ["Moon"]},
    (37, 3): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (37, 4): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (37, 5): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (37, 6): {"exalted": ["Venus"], "detriment": ["Moon"]},

    # Gate 38
    (38, 1): {"exalted": ["Mars"], "detriment": ["Pluto"]},
    (38, 2): {"exalted": ["Pluto"], "detriment": ["Moon"]},
    (38, 3): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (38, 4): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (38, 5): {"exalted": ["Sun"], "detriment": ["Earth"]},
    (38, 6): {"exalted": ["Earth"], "detriment": ["Pluto"]},

    # Gate 39
    (39, 1): {"exalted": ["Mars"], "detriment": ["Mercury"]},
    (39, 2): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (39, 3): {"exalted": ["Earth"], "detriment": ["Jupiter"]},
    (39, 4): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (39, 5): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (39, 6): {"exalted": ["Moon"], "detriment": ["Mars"]},

    # Gate 40
    (40, 1): {"exalted": ["Sun"], "detriment": ["Moon"]},
    (40, 2): {"exalted": ["Sun"], "detriment": ["Moon"]},
    (40, 3): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (40, 4): {"exalted": ["Sun"], "detriment": ["Pluto"]},
    (40, 5): {"exalted": ["Sun"], "detriment": ["Earth"]},
    (40, 6): {"exalted": ["Sun"], "detriment": ["Earth"]},

    # Gate 41
    (41, 1): {"exalted": ["Neptune"], "detriment": ["Mars"]},
    (41, 2): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (41, 3): {"exalted": ["Saturn"], "detriment": ["Pluto"]},
    (41, 4): {"exalted": ["Earth"], "detriment": ["Mars"]},
    (41, 5): {"exalted": ["Mars"], "detriment": ["Venus"]},
    (41, 6): {"exalted": ["Pluto"], "detriment": ["Moon"]},

    # Gate 42
    (42, 1): {"exalted": ["Sun"], "detriment": ["Venus"]},
    (42, 2): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (42, 3): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (42, 4): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (42, 5): {"exalted": ["Sun"], "detriment": ["Moon"]},
    (42, 6): {"exalted": ["Sun"], "detriment": ["Mars"]},

    # Gate 43
    (43, 1): {"exalted": ["Pluto"], "detriment": ["Venus"]},
    (43, 2): {"exalted": ["Pluto"], "detriment": ["Moon"]},
    (43, 3): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (43, 4): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (43, 5): {"exalted": ["Moon"], "detriment": ["Venus"]},
    (43, 6): {"exalted": ["Sun"], "detriment": ["Jupiter"]},

    # Gate 44
    (44, 1): {"exalted": ["Pluto"], "detriment": ["Venus"]},
    (44, 2): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (44, 3): {"exalted": ["Mars"], "detriment": ["Moon"]},
    (44, 4): {"exalted": ["Pluto"], "detriment": ["Jupiter"]},
    (44, 5): {"exalted": ["Sun"], "detriment": ["Mars"]},
    (44, 6): {"exalted": ["Pluto"], "detriment": ["Saturn"]},

    # Gate 45
    (45, 1): {"exalted": ["Mars"], "detriment": ["Venus"]},
    (45, 2): {"exalted": ["Mars"], "detriment": ["Sun"]},
    (45, 3): {"exalted": ["Jupiter"], "detriment": ["Uranus"]},
    (45, 4): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (45, 5): {"exalted": ["Jupiter"], "detriment": ["Moon"]},
    (45, 6): {"exalted": ["Uranus"], "detriment": ["Sun"]},

    # Gate 46
    (46, 1): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (46, 2): {"exalted": ["Sun"], "detriment": ["Mars"]},
    (46, 3): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (46, 4): {"exalted": ["Earth"], "detriment": ["Mars"]},
    (46, 5): {"exalted": ["Neptune"], "detriment": ["Moon"]},
    (46, 6): {"exalted": ["Neptune"], "detriment": ["Mars"]},

    # Gate 47
    (47, 1): {"exalted": ["Saturn"], "detriment": ["Sun"]},
    (47, 2): {"exalted": ["Mars"], "detriment": ["Moon"]},
    (47, 3): {"exalted": ["Saturn"], "detriment": ["Mars"]},
    (47, 4): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (47, 5): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (47, 6): {"exalted": ["Sun"], "detriment": ["Jupiter"]},

    # Gate 48
    (48, 1): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (48, 2): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (48, 3): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (48, 4): {"exalted": ["Sun"], "detriment": ["Earth"]},
    (48, 5): {"exalted": ["Mars"], "detriment": ["Moon"]},
    (48, 6): {"exalted": ["Venus"], "detriment": ["Mars"]},

    # Gate 49
    (49, 1): {"exalted": ["Jupiter"], "detriment": ["Sun"]},
    (49, 2): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (49, 3): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (49, 4): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (49, 5): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (49, 6): {"exalted": ["Sun"], "detriment": ["Neptune"]},

    # Gate 50
    (50, 1): {"exalted": ["Mars"], "detriment": ["Moon"]},
    (50, 2): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (50, 3): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (50, 4): {"exalted": ["Saturn"], "detriment": ["Mars"]},
    (50, 5): {"exalted": ["Saturn"], "detriment": ["Moon"]},
    (50, 6): {"exalted": ["Venus"], "detriment": ["Mars"]},

    # Gate 51
    (51, 1): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (51, 2): {"exalted": ["Mars"], "detriment": ["Mercury"]},
    (51, 3): {"exalted": ["Sun"], "detriment": ["Jupiter"]},
    (51, 4): {"exalted": ["Uranus"], "detriment": ["Mercury"]},
    (51, 5): {"exalted": ["Sun"], "detriment": ["Mars"]},
    (51, 6): {"exalted": ["Sun"], "detriment": ["Pluto"]},

    # Gate 52
    (52, 1): {"exalted": ["Earth"], "detriment": ["Mars"]},
    (52, 2): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (52, 3): {"exalted": ["Saturn"], "detriment": ["Mars"]},
    (52, 4): {"exalted": ["Saturn"], "detriment": ["Jupiter"]},
    (52, 5): {"exalted": ["Earth"], "detriment": ["Mars"]},
    (52, 6): {"exalted": ["Earth"], "detriment": ["Mars"]},

    # Gate 53
    (53, 1): {"exalted": ["Neptune"], "detriment": ["Venus"]},
    (53, 2): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (53, 3): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (53, 4): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (53, 5): {"exalted": ["Earth"], "detriment": ["Mars"]},
    (53, 6): {"exalted": ["Moon"], "detriment": ["Pluto"]},

    # Gate 54
    (54, 1): {"exalted": ["Pluto"], "detriment": ["Venus"]},
    (54, 2): {"exalted": ["Saturn"], "detriment": ["Mars"]},
    (54, 3): {"exalted": ["Pluto"], "detriment": ["Venus"]},
    (54, 4): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (54, 5): {"exalted": ["Sun"], "detriment": ["Mars"]},
    (54, 6): {"exalted": ["Saturn"], "detriment": ["Mars"]},

    # Gate 55
    (55, 1): {"exalted": ["Jupiter"], "detriment": ["Venus"]},
    (55, 2): {"exalted": ["Saturn"], "detriment": ["Venus"]},
    (55, 3): {"exalted": ["Saturn"], "detriment": ["Mars"]},
    (55, 4): {"exalted": ["Neptune"], "detriment": ["Jupiter"]},
    (55, 5): {"exalted": ["Sun"], "detriment": ["Moon"]},
    (55, 6): {"exalted": ["Sun"], "detriment": ["Saturn"]},

    # Gate 56
    (56, 1): {"exalted": ["Mars"], "detriment": ["Venus"]},
    (56, 2): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (56, 3): {"exalted": ["Sun"], "detriment": ["Mars"]},
    (56, 4): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (56, 5): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (56, 6): {"exalted": ["Sun"], "detriment": ["Mars"]},

    # Gate 57
    (57, 1): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (57, 2): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (57, 3): {"exalted": ["Mercury"], "detriment": ["Mars"]},
    (57, 4): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (57, 5): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (57, 6): {"exalted": ["Moon"], "detriment": ["Mars"]},

    # Gate 58
    (58, 1): {"exalted": ["Venus"], "detriment": ["Moon"]},
    (58, 2): {"exalted": ["Sun"], "detriment": ["Uranus"]},
    (58, 3): {"exalted": ["Pluto"], "detriment": ["Mars"]},
    (58, 4): {"exalted": ["Pluto"], "detriment": ["Jupiter"]},
    (58, 5): {"exalted": ["Moon"], "detriment": ["Sun"]},
    (58, 6): {"exalted": ["Moon"], "detriment": ["Mercury"]},

    # Gate 59
    (59, 1): {"exalted": ["Sun"], "detriment": ["Mercury"]},
    (59, 2): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (59, 3): {"exalted": ["Mars"], "detriment": ["Venus"]},
    (59, 4): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (59, 5): {"exalted": ["Sun"], "detriment": ["Uranus"]},
    (59, 6): {"exalted": ["Venus"], "detriment": ["Mercury"]},

    # Gate 60
    (60, 1): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (60, 2): {"exalted": ["Saturn"], "detriment": ["Mars"]},
    (60, 3): {"exalted": ["Saturn"], "detriment": ["Mars"]},
    (60, 4): {"exalted": ["Mercury"], "detriment": ["Mars"]},
    (60, 5): {"exalted": ["Neptune"], "detriment": ["Mars"]},
    (60, 6): {"exalted": ["Mercury"], "detriment": ["Mars"]},

    # Gate 61
    (61, 1): {"exalted": ["Pluto"], "detriment": ["Venus"]},
    (61, 2): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (61, 3): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (61, 4): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (61, 5): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (61, 6): {"exalted": ["Pluto"], "detriment": ["Mars"]},

    # Gate 62
    (62, 1): {"exalted": ["Mars"], "detriment": ["Venus"]},
    (62, 2): {"exalted": ["Saturn"], "detriment": ["Mars"]},
    (62, 3): {"exalted": ["Uranus"], "detriment": ["Moon"]},
    (62, 4): {"exalted": ["Venus"], "detriment": ["Mars"]},
    (62, 5): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (62, 6): {"exalted": ["Saturn"], "detriment": ["Sun"]},

    # Gate 63
    (63, 1): {"exalted": ["Sun"], "detriment": ["Mars"]},
    (63, 2): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (63, 3): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (63, 4): {"exalted": ["Sun"], "detriment": ["Mars"]},
    (63, 5): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (63, 6): {"exalted": ["Mercury"], "detriment": ["Mars"]},

    # Gate 64
    (64, 1): {"exalted": ["Venus", "Mars"], "detriment": []},
    (64, 2): {"exalted": ["Venus"], "detriment": ["Sun"]},
    (64, 3): {"exalted": ["Moon"], "detriment": ["Mars"]},
    (64, 4): {"exalted": ["Sun"], "detriment": ["Moon"]},
    (64, 5): {"exalted": ["Jupiter"], "detriment": ["Mars"]},
    (64, 6): {"exalted": ["Mercury"], "detriment": ["Mars"]}
}


def get_planet_fixation(gate: int, line: int, planet: str) -> str:
    """
    Returns the Rave I Ching planetary fixation indicator:
    - '▲' for Exaltation
    - '▼' for Detriment
    - '' for Neutral / Open
    """
    fix_info = RAVE_LINE_FIXATIONS.get((gate, line))
    if not fix_info:
        return ""

    if planet in fix_info.get("exalted", []):
        return "▲"
    elif planet in fix_info.get("detriment", []):
        return "▼"
    return ""


def calculate_chart_fixations(gates_dict: Dict[str, Tuple[int, int]]) -> Dict[str, str]:
    """
    Calculate fixation indicators (▲ / ▼ / '') for all 13 celestial bodies.
    Input: { "Sun": (gate, line), "Earth": (gate, line), ... }
    Returns: { "Sun": "▲", "Earth": "", ... }
    """
    fixations = {}
    for planet, (gate, line) in gates_dict.items():
        fixations[planet] = get_planet_fixation(gate, line, planet)
    return fixations
