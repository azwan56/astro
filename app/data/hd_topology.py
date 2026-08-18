"""
Human Design Static Topology
Defines the 9 Centers, 64 Gates mapping to Centers, and 36 Channels.
"""

from typing import Dict, List, Tuple, Set

CENTERS = [
    "Head",
    "Ajna",
    "Throat",
    "G_Center",
    "Heart",
    "Sacral",
    "Spleen",
    "Solar_Plexus",
    "Root"
]

# Motor centers (important for Manifestor vs Projector vs Generator authority)
MOTOR_CENTERS = {"Solar_Plexus", "Sacral", "Heart", "Root"}

GATE_TO_CENTER: Dict[int, str] = {
    # Head Center
    64: "Head", 61: "Head", 63: "Head",
    
    # Ajna Center
    47: "Ajna", 24: "Ajna", 4: "Ajna", 11: "Ajna", 43: "Ajna", 17: "Ajna",
    
    # Throat Center
    62: "Throat", 23: "Throat", 56: "Throat", 35: "Throat", 12: "Throat",
    45: "Throat", 33: "Throat", 8: "Throat", 31: "Throat", 20: "Throat", 16: "Throat",
    
    # G Center
    1: "G_Center", 13: "G_Center", 25: "G_Center", 46: "G_Center",
    2: "G_Center", 15: "G_Center", 10: "G_Center", 7: "G_Center",
    
    # Heart / Ego Center
    21: "Heart", 40: "Heart", 26: "Heart", 51: "Heart",
    
    # Sacral Center
    5: "Sacral", 14: "Sacral", 29: "Sacral", 59: "Sacral",
    9: "Sacral", 3: "Sacral", 42: "Sacral", 27: "Sacral", 34: "Sacral",
    
    # Spleen Center
    48: "Spleen", 57: "Spleen", 44: "Spleen", 50: "Spleen",
    32: "Spleen", 28: "Spleen", 18: "Spleen",
    
    # Solar Plexus Center
    36: "Solar_Plexus", 22: "Solar_Plexus", 37: "Solar_Plexus",
    6: "Solar_Plexus", 49: "Solar_Plexus", 55: "Solar_Plexus", 30: "Solar_Plexus",
    
    # Root Center
    53: "Root", 60: "Root", 52: "Root", 19: "Root",
    39: "Root", 41: "Root", 58: "Root", 38: "Root", 54: "Root"
}

# 36 Channels: Tuple of (GateA, GateB, Name, CenterA, CenterB)
CHANNELS_DATA = [
    # Head - Ajna
    (64, 47, "Channel of Abstraction", "Head", "Ajna"),
    (61, 24, "Channel of Awareness", "Head", "Ajna"),
    (63, 4, "Channel of Logic", "Head", "Ajna"),
    
    # Ajna - Throat
    (17, 62, "Channel of Acceptance", "Ajna", "Throat"),
    (43, 23, "Channel of Structuring", "Ajna", "Throat"),
    (11, 56, "Channel of Curiosity", "Ajna", "Throat"),
    
    # Throat - G_Center
    (31, 7, "Channel of The Alpha", "Throat", "G_Center"),
    (8, 1, "Channel of Inspiration", "Throat", "G_Center"),
    (33, 13, "Channel of The Prodigal", "Throat", "G_Center"),
    (20, 10, "Channel of Awakening", "Throat", "G_Center"),
    
    # Throat - Heart
    (45, 21, "Channel of Money", "Throat", "Heart"),
    
    # Throat - Solar_Plexus
    (12, 22, "Channel of Openness", "Throat", "Solar_Plexus"),
    (35, 36, "Channel of Transitoriness", "Throat", "Solar_Plexus"),
    
    # Throat - Sacral
    (20, 34, "Channel of Charisma", "Throat", "Sacral"),
    
    # Throat - Spleen
    (20, 57, "Channel of Brainwave", "Throat", "Spleen"),
    (16, 48, "Channel of The Wavelength", "Throat", "Spleen"),
    
    # G_Center - Heart
    (25, 51, "Channel of Initiation", "G_Center", "Heart"),
    
    # G_Center - Sacral
    (15, 5, "Channel of Rhythm", "G_Center", "Sacral"),
    (2, 14, "Channel of The Beat", "G_Center", "Sacral"),
    (46, 29, "Channel of Discovery", "G_Center", "Sacral"),
    (10, 34, "Channel of Exploration", "G_Center", "Sacral"),
    
    # G_Center - Spleen
    (10, 57, "Channel of Perfect Form", "G_Center", "Spleen"),
    
    # Heart - Solar_Plexus
    (40, 37, "Channel of Community", "Heart", "Solar_Plexus"),
    
    # Heart - Spleen
    (26, 44, "Channel of Surrender", "Heart", "Spleen"),
    
    # Sacral - Solar_Plexus
    (59, 6, "Channel of Mating", "Sacral", "Solar_Plexus"),
    
    # Sacral - Spleen
    (27, 50, "Channel of Preservation", "Sacral", "Spleen"),
    (34, 57, "Channel of Power", "Sacral", "Spleen"),
    
    # Sacral - Root
    (42, 53, "Channel of Maturation", "Sacral", "Root"),
    (3, 60, "Channel of Mutation", "Sacral", "Root"),
    (9, 52, "Channel of Concentration", "Sacral", "Root"),
    
    # Root - Solar_Plexus
    (19, 49, "Channel of Synthesis", "Root", "Solar_Plexus"),
    (39, 55, "Channel of Emoting", "Root", "Solar_Plexus"),
    (41, 30, "Channel of Recognition", "Root", "Solar_Plexus"),
    
    # Root - Spleen
    (58, 18, "Channel of Judgement", "Root", "Spleen"),
    (38, 28, "Channel of Struggle", "Root", "Spleen"),
    (54, 32, "Channel of Transformation", "Root", "Spleen")
]

# Quick lookup helper maps
CHANNEL_MAP: Dict[Tuple[int, int], dict] = {}
GATE_PARTNERS: Dict[int, Set[int]] = {g: set() for g in GATE_TO_CENTER.keys()}

for g1, g2, name, c1, c2 in CHANNELS_DATA:
    info = {"gate_a": g1, "gate_b": g2, "name": name, "center_a": c1, "center_b": c2}
    CHANNEL_MAP[(g1, g2)] = info
    CHANNEL_MAP[(g2, g1)] = info
    GATE_PARTNERS[g1].add(g2)
    GATE_PARTNERS[g2].add(g1)
