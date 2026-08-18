"""
Authority Hierarchy & Type Determination Engine
Calculates:
- Defined Centers & Channels
- Energy Type (Generator, Manifesting Generator, Manifestor, Projector, Reflector)
- Inner Authority Hierarchy
- Profile (Personality Line / Design Line)
- Definition Type (Single, Split, Triple Split, Quadruple Split, None)
- Energy Bridge Topology & Subgraph Components
"""

from typing import Dict, List, Set, Tuple
from app.data.hd_topology import (
    CENTERS, MOTOR_CENTERS, GATE_TO_CENTER, CHANNELS_DATA, CHANNEL_MAP
)

CENTER_NAMES_CN = {
    "Head": "头脑中心", "Ajna": "逻辑中心", "Throat": "喉咙中心",
    "G_Center": "G中心", "Heart": "意志力/心中心", "Sacral": "荐骨中心",
    "Spleen": "脾/直觉中心", "Solar_Plexus": "情绪中心", "Root": "根部中心"
}


def analyze_human_design_chart(
    personality_gates: Dict[str, Tuple[int, int]],
    design_gates: Dict[str, Tuple[int, int]]
) -> dict:
    """
    Main chart analysis engine with Topology Graph & Bridge Analysis.
    """
    pers_gate_set = {g for g, _ in personality_gates.values()}
    des_gate_set = {g for g, _ in design_gates.values()}
    all_active_gates = pers_gate_set.union(des_gate_set)
    
    # 1. Determine Defined Channels
    defined_channels = []
    active_channel_pairs = set()
    
    for g1, g2, name, c1, c2 in CHANNELS_DATA:
        if g1 in all_active_gates and g2 in all_active_gates:
            active_channel_pairs.add((g1, g2))
            active_channel_pairs.add((g2, g1))
            
            # Color classification
            is_pers_g1 = g1 in pers_gate_set
            is_pers_g2 = g2 in pers_gate_set
            is_des_g1 = g1 in des_gate_set
            is_des_g2 = g2 in des_gate_set
            
            if (is_pers_g1 and is_pers_g2) and not (is_des_g1 and is_des_g2):
                color = "Personality"
            elif (is_des_g1 and is_des_g2) and not (is_pers_g1 and is_pers_g2):
                color = "Design"
            else:
                color = "Both"
                
            defined_channels.append({
                "gate_a": g1,
                "gate_b": g2,
                "name": name,
                "center_a": c1,
                "center_b": c2,
                "color": color
            })

    # 2. Determine Defined Centers
    defined_centers: Set[str] = set()
    for ch in defined_channels:
        defined_centers.add(ch["center_a"])
        defined_centers.add(ch["center_b"])
        
    undefined_centers = set(CENTERS) - defined_centers

    # 3. Graph Connectivity
    center_adj: Dict[str, Set[str]] = {c: set() for c in CENTERS}
    for ch in defined_channels:
        c1, c2 = ch["center_a"], ch["center_b"]
        center_adj[c1].add(c2)
        center_adj[c2].add(c1)

    def is_center_connected(start_center: str, target_center: str) -> bool:
        if start_center not in defined_centers or target_center not in defined_centers:
            return False
        visited = set()
        queue = [start_center]
        while queue:
            curr = queue.pop(0)
            if curr == target_center:
                return True
            visited.add(curr)
            for nxt in center_adj[curr]:
                if nxt in defined_centers and nxt not in visited:
                    queue.append(nxt)
        return False

    has_motor_to_throat = any(
        is_center_connected(m, "Throat") for m in MOTOR_CENTERS if m in defined_centers
    )

    # 4. Energy Type Determination
    is_sacral_defined = "Sacral" in defined_centers
    
    if len(defined_centers) == 0:
        energy_type = "Reflector"
        strategy = "Wait a Lunar Cycle (28.5 Days)"
        signature = "Surprise"
        not_self = "Disappointment"
    elif is_sacral_defined:
        if has_motor_to_throat:
            energy_type = "Manifesting Generator"
        else:
            energy_type = "Pure Generator"
        strategy = "To Respond"
        signature = "Satisfaction"
        not_self = "Frustration"
    elif has_motor_to_throat:
        energy_type = "Manifestor"
        strategy = "To Inform"
        signature = "Peace"
        not_self = "Anger"
    else:
        energy_type = "Projector"
        strategy = "Wait for the Invitation"
        signature = "Success"
        not_self = "Bitterness"

    # 5. Authority Hierarchy Determination
    is_reflector = energy_type == "Reflector"
    
    if is_reflector or len(defined_centers) == 0:
        authority = "Lunar Authority"
    elif "Solar_Plexus" in defined_centers:
        authority = "Emotional Authority"
    elif "Sacral" in defined_centers:
        authority = "Sacral Authority"
    elif "Spleen" in defined_centers:
        authority = "Splenic Authority"
    elif "Heart" in defined_centers:
        authority = "Ego Authority"
    elif "G_Center" in defined_centers:
        authority = "Self-Projected Authority"
    elif any(c in defined_centers for c in ["Throat", "Ajna", "Head"]):
        authority = "Mental / Environmental Authority"
    else:
        authority = "No Inner Authority"

    # 6. Profile
    pers_sun_line = personality_gates["Sun"][1]
    des_sun_line = design_gates["Sun"][1]
    profile = f"{pers_sun_line}/{des_sun_line}"

    # 7. Subgraph Connected Components
    components = []
    unvisited_def = set(defined_centers)
    while unvisited_def:
        start = unvisited_def.pop()
        comp = [start]
        q = [start]
        while q:
            curr = q.pop(0)
            for nxt in center_adj[curr]:
                if nxt in unvisited_def:
                    unvisited_def.remove(nxt)
                    q.append(nxt)
                    comp.append(nxt)
        components.append(comp)

    subgraph_count = len(components)

    if subgraph_count == 0:
        definition_type = "No Definition"
    elif subgraph_count == 1:
        definition_type = "Single Definition"
    elif subgraph_count == 2:
        definition_type = "Split Definition"
    elif subgraph_count == 3:
        definition_type = "Triple Split Definition"
    else:
        definition_type = "Quadruple Split Definition"

    # 8. Bridge Channel Identification (For Split / Multi-split Definition)
    # Map each center to its component index
    center_to_comp = {}
    for idx, comp in enumerate(components):
        for c in comp:
            center_to_comp[c] = idx

    bridge_channels = []
    for g1, g2, name, c1, c2 in CHANNELS_DATA:
        if (g1, g2) not in active_channel_pairs and (g2, g1) not in active_channel_pairs:
            # Check if c1 and c2 belong to different defined components
            if c1 in center_to_comp and c2 in center_to_comp:
                comp1 = center_to_comp[c1]
                comp2 = center_to_comp[c2]
                if comp1 != comp2:
                    is_g1_active = g1 in all_active_gates
                    is_g2_active = g2 in all_active_gates
                    
                    bridge_type = "Small Split Bridge" if (is_g1_active or is_g2_active) else "Wide Split Bridge"
                    needed_gate = g2 if is_g1_active else (g1 if is_g2_active else None)
                    
                    bridge_channels.append({
                        "channel_name": name,
                        "gate_a": g1,
                        "gate_b": g2,
                        "center_a": c1,
                        "center_b": c2,
                        "comp_a_idx": comp1,
                        "comp_b_idx": comp2,
                        "bridge_type": bridge_type,
                        "needed_gate": needed_gate,
                        "is_g1_active": is_g1_active,
                        "is_g2_active": is_g2_active
                    })

    # 9. Hanging Gates Identification
    defined_channel_gates = set()
    for ch in defined_channels:
        defined_channel_gates.add(ch["gate_a"])
        defined_channel_gates.add(ch["gate_b"])

    hanging_gates = [g for g in all_active_gates if g not in defined_channel_gates]

    return {
        "energy_type": energy_type,
        "strategy": strategy,
        "signature": signature,
        "not_self_theme": not_self,
        "authority": authority,
        "profile": profile,
        "definition_type": definition_type,
        "defined_centers": list(defined_centers),
        "undefined_centers": list(undefined_centers),
        "defined_channels": defined_channels,
        "active_gates": list(all_active_gates),
        "personality_gates": personality_gates,
        "design_gates": design_gates,
        "subgraph_count": subgraph_count,
        "components": components,
        "bridge_channels": bridge_channels,
        "hanging_gates": hanging_gates
    }
