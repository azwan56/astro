"""
Extended Human Design PHS, Four Variables, Gene Keys, BG5, Dream Rave, Love & Relationships, Penta Team Modules
Includes Daily Transit Forecast Engine and Suspenseful Rich Main Theme Generator (富文本与悬念钩子关键主题解盘).
"""

import datetime
from typing import Dict, List, Tuple
from app.core.ephemeris import calculate_planet_longitudes
from app.core.mandala import longitude_to_gate_line
from app.data.hd_topology import CHANNELS_DATA, GATE_TO_CENTER

PHS_DIGESTION_TYPES = {
    1: {"name_cn": "原始/连续饮食 (Appetite)", "desc_cn": "【1号色彩·洞穴/原始饮食】一次只吃一种食物，避免混合多种复杂食材，适合简单自然的进食节奏。"},
    2: {"name_cn": "挑选/固执饮食 (Taste)", "desc_cn": "【2号色彩·偏好/挑食模式】极度依赖个人口味偏好，只吃自己认可和喜欢的食物，不要强迫尝试不喜欢的菜品。"},
    3: {"name_cn": "温度/液体饮食 (Thirst)", "desc_cn": "【3号色彩·温度与水分】食物的温度高于或低于体温至关重要，适合多补充温热或清凉的液体食物。"},
    4: {"name_cn": "环境/氛围饮食 (Touch)", "desc_cn": "【4号色彩·进食氛围】进食时的社交氛围与环境平静度比食物本身更重要，在轻松愉悦的气氛下消化最好。"},
    5: {"name_cn": "声频/音律饮食 (Sound)", "desc_cn": "【5号色彩·背景声频】进食时周围的声音与音乐频率直接影响消化系统，适合在特定声频或安静音乐中进食。"},
    6: {"name_cn": "光照/日光饮食 (Light)", "desc_cn": "【6号色彩·日光与光线】受阳光与昼夜光线影响，适合在白天阳光充足时进食，夜间减少进食。"}
}

PHS_ENVIRONMENT_TYPES = {
    1: {"name_cn": "洞穴 (Caves)", "desc_cn": "【1号环境·洞穴】需要极高的安全感与私密性，喜欢背靠墙壁、能够掌握出口与大门的封闭舒适空间。"},
    2: {"name_cn": "市集 (Markets)", "desc_cn": "【2号环境·市集】喜欢人流密集、资讯与商业能量交换频繁的地方，在热闹的都市或咖啡馆中最能激发活力。"},
    3: {"name_cn": "厨房 (Kitchens)", "desc_cn": "【3号环境·厨房】核心在于“能量转化”，喜欢能看到食材、创意或科技被转化加工的过程的空间。"},
    4: {"name_cn": "山脉 (Mountains)", "desc_cn": "【4号环境·山脉】喜欢置身于高处、拥有开阔视野，能够从高处俯瞰下方动向的地方，需要高度的独立与稀薄空气感。"},
    5: {"name_cn": "山谷 (Valleys)", "desc_cn": "【5号环境·山谷】喜欢拥有交流感、回声与信息流动的低洼或山谷地带，适合通过深度沟通与他人连接。"},
    6: {"name_cn": "海岸 (Shores)", "desc_cn": "【6号环境·海岸】处于边界与过渡地带（如陆地与海洋、城市与乡村交界处），喜欢能看到事物交接与转变的空间。"}
}

PHS_PERSPECTIVE_TYPES = {
    1: {"name_cn": "生存 (Survival)", "desc_cn": "【1号视角·生存】关注事物的基础稳定性与安全感，敏锐研究事物“如何运转”与基础保障。"},
    2: {"name_cn": "可能 (Possibility)", "desc_cn": "【2号视角·可能】关注未被开发的潜能，眼睛总是盯着“未来会有什么全新的机会与可能性”。"},
    3: {"name_cn": "权力 (Power)", "desc_cn": "【3号视角·权力】关注社会层次、影响力以及谁拥有话语权，敏锐感知社会的互动架构。"},
    4: {"name_cn": "需求 (Need)", "desc_cn": "【4号视角·需求】关注匮乏与需求，能敏锐察觉到别人需要什么，或者什么资源目前是短缺的。"},
    5: {"name_cn": "概率 (Probability)", "desc_cn": "【5号视角·概率】关注特定情境下的特定结果，倾向于计算概率，判断事情成功的机率。"},
    6: {"name_cn": "个人/独特性 (Personal)", "desc_cn": "【6号视角·个人】关注个人特质与独特性的展示，观察人们如何呈现自我及表现出来。"}
}

PHS_MOTIVATION_TYPES = {
    1: {"name_cn": "恐惧 (Fear)", "desc_cn": "【1号动机·恐惧】底层驱动力来自确保安全，通过彻底了解、研究与调研来消除未知恐惧。"},
    2: {"name_cn": "希望 (Hope)", "desc_cn": "【2号动机·希望】底层驱动力来自对未来的坚定信念，在信任宇宙流程中自然前行。"},
    3: {"name_cn": "欲望 (Desire)", "desc_cn": "【3号动机·欲望】底层驱动力来自对体验的强烈渴望，想要亲自去感受和尝试各种事物。"},
    4: {"name_cn": "需求 (Need)", "desc_cn": "【4号动机·需求】底层驱动力来自填补空白，通过给予和满足他人的需求来建立价值。"},
    5: {"name_cn": "控制 (Control)", "desc_cn": "【5号动机·控制】底层驱动力来自掌控局势或指引他人，追求秩序、效率与掌控感。"},
    6: {"name_cn": "纯真 (Innocence)", "desc_cn": "【6号动机·纯真】底层驱动力来自放下特定目的，不带预设地去经历人生，随顺当下的自然流动。"}
}

GATES_OF_LOVE = {
    10: {"name_cn": "10号闸门：自我接纳之爱 (Love of Self)", "desc_cn": "【温柔拥抱真实的自己】您生命的真谛在于无条件地爱与接纳自己。"},
    15: {"name_cn": "15号闸门：全人类博爱 (Love of Humanity)", "desc_cn": "【广袤包容的温暖生命力】您对人类社会的极端多样性拥有天然的深刻包容。"},
    25: {"name_cn": "25号闸门：宇宙纯真之爱 (Universal Love)", "desc_cn": "【超越得失的治愈圣爱】您拥有一颗纯真无邪的心灵。"},
    46: {"name_cn": "46号闸门：肉体与体验之爱 (Love of Body)", "desc_cn": "【神圣身心合一的享受】您将身体视为灵魂在人间最神圣的尊贵神殿。"},
    28: {"name_cn": "28号闸门：意义与挣扎之爱 (Love of Purpose)", "desc_cn": "【灵魂深处的意义探索】您不满足于泛泛而谈的表层关系。"},
    58: {"name_cn": "58号闸门：喜悦与完美之爱 (Love of Life)", "desc_cn": "【感染周遭的生命欢愉】您对改善生活品质充满无限积极能量。"},
    41: {"name_cn": "41号闸门：憧憬与梦想之爱 (Love of Dreams)", "desc_cn": "【浪漫美好的深情期待】您的内心藏着丰富而浪漫的梦幻世界。"},
    44: {"name_cn": "44号闸门：灵魂陪伴之爱 (Love of Bonding)", "desc_cn": "【敏锐的灵魂伴侣嗅觉】您在人际与亲密关系中拥有极度敏锐的直觉洞察力。"}
}

GENE_KEYS_SAMPLE = {
    1: {"shadow": "熵 (Entropy)", "gift": "创造力 (Creativity)", "siddhi": "美 (Beauty)"},
    2: {"shadow": "迷失 (Disconnection)", "gift": "方向 (Orientation)", "siddhi": "统一 (Unity)"},
    3: {"shadow": "混乱 (Chaos)", "gift": "创新 (Innovation)", "siddhi": "纯真 (Innocence)"},
    4: {"shadow": "怀疑 (Intolerance)", "gift": "理解 (Understanding)", "siddhi": "宽恕 (Forgiveness)"},
    5: {"shadow": "急躁 (Impatience)", "gift": "等待 (Timelessness)", "siddhi": "平静 (Peace)"},
    6: {"shadow": "冲突 (Conflict)", "gift": "外交 (Diplomacy)", "siddhi": "和平 (Peace)"},
    10: {"shadow": "自私 (Selfishness)", "gift": "自爱 (Self-Acceptance)", "siddhi": "存在 (Being)"},
    19: {"shadow": "依赖 (Dependence)", "gift": "敏感 (Sensitivity)", "siddhi": "牺牲 (Sacrifice)"},
    20: {"shadow": "浅薄 (Superficiality)", "gift": "临在 (Presence)", "siddhi": "静止 (Clarity)"},
    34: {"shadow": "强暴 (Force)", "gift": "力量 (Strength)", "siddhi": "威严 (Majesty)"},
    57: {"shadow": "焦虑 (Anxiety)", "gift": "直觉 (Intuition)", "siddhi": "明晰 (Clarity)"},
    64: {"shadow": "困惑 (Confusion)", "gift": "想象 (Imagination)", "siddhi": "光辉 (Illumination)"}
}

CENTER_NAMES_CN = {
    "Head": "头脑中心", "Ajna": "逻辑中心", "Throat": "喉咙中心",
    "G_Center": "G中心", "Heart": "意志力/心中心", "Sacral": "荐骨中心",
    "Spleen": "脾/直觉中心", "Solar_Plexus": "情绪中心", "Root": "根部中心"
}


def get_rich_main_theme_coaching(chart_result: dict) -> dict:
    """
    Rich & Suspenseful Main Theme Generator (富文本与悬念钩子免费关键主题解盘).
    Provides deep baseline insights while hooking users for paid deep modules.
    """
    energy_type = chart_result.get("energy_type", "Pure Generator")
    strategy = chart_result.get("strategy", "To Respond")
    authority = chart_result.get("authority", "Sacral Authority")
    not_self = chart_result.get("not_self_theme", "Frustration")
    profile = chart_result.get("profile", "5/1")
    def_type = chart_result.get("definition_type", "Single Definition")
    active_gates_cnt = len(chart_result.get("active_gates", []))
    defined_channels_cnt = len(chart_result.get("defined_channels", []))

    type_cn_map = {
        "Pure Generator": "纯粹生产者", "Manifesting Generator": "显化生产者",
        "Manifestor": "显化者", "Projector": "引导者/显示生产者/投射者", "Reflector": "反映者"
    }
    type_cn = type_cn_map.get(energy_type, energy_type)

    auth_cn_map = {
        "Emotional Authority": "情绪权威", "Sacral Authority": "荐骨权威",
        "Splenic Authority": "脾/直觉权威", "Ego Authority": "意志力权威",
        "Self-Projected Authority": "自我投射权威", "Mental / Environmental Authority": "头脑/环境权威",
        "Lunar Authority": "月亮权威", "No Inner Authority": "无内在权威"
    }
    auth_cn = auth_cn_map.get(authority, authority)

    strat_cn_map = {
        "To Respond": "等待荐骨的回应", "To Inform": "告知后再发起",
        "Wait for the Invitation": "等待邀请", "Wait a Lunar Cycle (28.5 Days)": "等待一个月亮周期 (28.5天)"
    }
    strat_cn = strat_cn_map.get(strategy, strategy)

    not_self_cn_map = {
        "Frustration": "感到强烈的挫败感", "Anger": "感到愤怒与阻力",
        "Bitterness": "感到苦涩与未被识别", "Disappointment": "感到失望与困惑"
    }
    not_self_cn = not_self_cn_map.get(not_self, not_self)

    # 1. 深度架构解盘
    arch_insight = f"作为一名 **【{type_cn}】**（人生角色 {profile}），您天然携带了极其丰沛的生命引擎。在日常生活中，当您顺应 **【{strat_cn}】** 时，您的能量场会展现出无可比拟的顺畅与吸引力。相反，若用头脑强行规划冲动发起，则会陷入 **【{not_self_cn}】** 的非自我磨损中。"

    # 2. 内在导航解盘
    auth_insight = f"您的底层决策导航星为 **【{auth_cn}】**。在面对人生重大决策、职业转型或情感抉择时，请永远不要依赖头脑的死记硬背与逻辑焦虑。听从身体发出的第一个直觉/荐骨物理响应，那是您灵魂最可靠的指南针。"

    # 3. 悬念钩子 1：人际吸引与能量桥接断裂盲区 (Hook 1: Split & Love)
    hook_split = f"✦ **【隐秘悬念 · 人际吸引的暗码】**：您的排盘呈现为【{def_type}】，体内激活了 {defined_channels_cnt} 条稳定通道与 {active_gates_cnt} 个印记卦门。但在您的能量蓝图深处，隐藏着一个极其关键的**能量桥接断裂区**！这解释了您为何会在过去的恋爱或职场合作中，无意识地被某种特定性格的人强烈吸引并感到'非他不可'……想揭开究竟是哪个神圣卦门在暗中掌控您的亲密关系？请解锁 **【⚡ 能量桥接诊断】** 与 **【💖 爱与关系 5维报告】**。"

    # 4. 悬念钩子 2：夜间梦境与身体高维进食密码 (Hook 2: Dream & PHS)
    hook_phs = f"✦ **【隐秘悬念 · 身体潜意识与夜间梦境】**：在白天，您的显意识掌控着日常生活；但当您夜间入睡时，您的头脑退去，潜意识会进入特定的**梦境领域**吸收并净化外在电荷！此外，您的大脑拥有独特的 Color 消化律与物理 Environment 居住环境模式。想知道您最适合在什么声频/日光下进食，以及如何在睡眠中复位线粒体活力？请解锁 **【🍎 PHS原始健康】** 与 **【🌙 睡眠梦图 5维报告】**。"

    # 5. 悬念钩子 3：商业赚钱与 3-5 人团队潜能 (Hook 3: BG5 & Penta)
    hook_bg5 = f"✦ **【隐秘悬念 · 商业变现与团队柱石】**：在商业与财富领域，您定义的能量中心隐藏着您天然的**商业定价权与变现杀手锏**，而在 3~5 人小团队中您更担任着特定的 Penta 商业柱石位。想知道您如何避开商业竞争陷阱、精准定位最高价值角色？请解锁 **【💼 BG5 商业定位】** 与 **【👥 BG5 Penta 团队能力】**。"

    return {
        "type_cn": type_cn,
        "profile": profile,
        "strategy_cn": strat_cn,
        "authority_cn": auth_cn,
        "not_self_cn": not_self_cn,
        "arch_insight": arch_insight,
        "auth_insight": auth_insight,
        "hook_split": hook_split,
        "hook_phs": hook_phs,
        "hook_bg5": hook_bg5
    }


def get_daily_transit_coaching(natal_chart: dict, target_date_str: str = "") -> dict:
    """
    Calculates Daily/Future Human Design Transit Forecast (流日/未来天候能量教练预测).
    """
    if target_date_str:
        try:
            target_dt = datetime.datetime.strptime(f"{target_date_str} 12:00", "%Y-%m-%d %H:%M")
        except Exception:
            target_dt = datetime.datetime.utcnow()
    else:
        target_dt = datetime.datetime.utcnow()

    transit_lons = calculate_planet_longitudes(target_dt)
    transit_gates = { planet: longitude_to_gate_line(lon) for planet, lon in transit_lons.items() }

    sun_gate, sun_line = transit_gates["Sun"]
    moon_gate, moon_line = transit_gates["Moon"]
    earth_gate, earth_line = transit_gates["Earth"]

    transit_active_gates = { g for g, _ in transit_gates.values() }
    natal_gates = set(natal_chart.get("active_gates", []))
    combined_gates = natal_gates.union(transit_active_gates)

    natal_channels = { (c["gate_a"], c["gate_b"]) for c in natal_chart.get("defined_channels", []) }
    natal_channels_rev = { (c["gate_b"], c["gate_a"]) for c in natal_chart.get("defined_channels", []) }
    all_natal_ch_pairs = natal_channels.union(natal_channels_rev)

    transit_temporary_channels = []
    for g1, g2, name, c1, c2 in CHANNELS_DATA:
        if (g1, g2) not in all_natal_ch_pairs and (g2, g1) not in all_natal_ch_pairs:
            if g1 in combined_gates and g2 in combined_gates:
                is_g1_transit = g1 in transit_active_gates
                is_g2_transit = g2 in transit_active_gates
                trigger_gate = g1 if is_g1_transit else g2
                transit_temporary_channels.append({
                    "channel_name": name,
                    "gate_a": g1, "gate_b": g2,
                    "trigger_gate": trigger_gate,
                    "center_a": CENTER_NAMES_CN.get(c1, c1),
                    "center_b": CENTER_NAMES_CN.get(c2, c2)
                })

    date_display = target_dt.strftime("%Y年%m月%d日")
    
    theme_text = f"【今日太阳过境焦点：{sun_gate}号卦门第{sun_line}爻 | 月亮过境：{moon_gate}号卦门】"
    if sun_gate in natal_gates:
        theme_text += f" 今日本命太阳与流日太阳形成【高频共振】！您在{sun_gate}号卦门的天然优势将被强力放大。"

    if transit_temporary_channels:
        temp_ch_texts = [f"✦ 【流日高能接通】{ch['channel_name']}通道（{ch['gate_a']}-{ch['gate_b']}号）：连接【{ch['center_a']}】与【{ch['center_b']}】。今日流日天体激活了 {ch['trigger_gate']}号卦门，临时填补了您的能量，为您带来突破性灵感！" for ch in transit_temporary_channels]
        ch_analysis = "\n".join(temp_ch_texts)
    else:
        ch_analysis = "✦ 今日本命能量稳定运化。没有强烈的流日跨中心电击冲撞，适合沉淀深耕、按部就班地推进核心项目。"

    career_guide = f"【{date_display} 职场与商业沟通指南】今日太阳{sun_gate}号卦门聚焦于行动与思考。顺应您的策略与内在权威做决策。若需开启关键商务对话或重要决策，宜选在午后情绪平缓时进行。"

    not_self_warning = f"【{date_display} 非自我与防雷提醒】今日月亮过境 {moon_gate}号卦门，可能带来短暂的情绪起伏或焦虑感。警惕头脑急于证明自己的冲动，允许情绪流过而不做过激反应。"

    affirmation = f"【{date_display} 大师心理教练能量日签】'信任你体内的内在权威。宇宙今日在默默为你铺路，全然在场，活出你天然的喜悦与力量！'"

    return {
        "transit_date": date_display,
        "sun_transit": f"{sun_gate}号卦门 .{sun_line}爻",
        "moon_transit": f"{moon_gate}号卦门 .{moon_line}爻",
        "earth_transit": f"{earth_gate}号卦门 .{earth_line}爻",
        "daily_theme": theme_text,
        "transit_temporary_channels": transit_temporary_channels,
        "temp_channel_analysis": ch_analysis,
        "career_guide": career_guide,
        "not_self_warning": not_self_warning,
        "daily_affirmation": affirmation
    }


def get_energy_bridge_diagnostics(chart_result: dict) -> dict:
    """
    Automated Energy Bridge & De-conditioning Diagnostic Engine (能量桥接诊断算法).
    """
    def_type = chart_result.get("definition_type", "Single Definition")
    subgraph_count = chart_result.get("subgraph_count", 1)
    components = chart_result.get("components", [])
    bridge_channels = chart_result.get("bridge_channels", [])
    hanging_gates = chart_result.get("hanging_gates", [])
    defined_channels = chart_result.get("defined_channels", [])

    comp_names = []
    for idx, comp in enumerate(components):
        cn_list = [CENTER_NAMES_CN.get(c, c) for c in comp]
        comp_names.append(f"连通板块{idx+1}：{' + '.join(cn_list)}")

    if def_type == "Single Definition":
        def_analysis = "【单分定义 (Single Definition，占比 41.48%)】您的所有定义能量中心均由连通通道首尾相连接，形成一个闭合的能量流动环路。您的信息整合速度极快，天生具备很强的独立决策能力，不需要依赖他人就能感受到内心的完整与连贯。"
    elif def_type == "Split Definition":
        def_analysis = "【双分定义 (Split Definition，占比 45.90%)】您的体内存在 2 个彼此独立、未直接相连的能量连通板块。这种结构会在潜意识中带来一种持久的'断裂感'或'不完整感'。因此，您会无意识地被能够'架起能量桥梁'的人或环境吸引，渴望借由他人的能量闭合流转。"
    elif def_type == "Triple Split Definition":
        def_analysis = "【三分定义 (Triple Split Definition，占比 10.60%)】您的体内存在 3 个独立的能量连通板块。您处理与整合复杂信息需要更多时间。置身于多元人群与动态社交环境中，能帮助您自然地穿梭并融合这三股独立能量。"
    elif def_type == "Quadruple Split Definition":
        def_analysis = "【四分定义 (Quadruple Split Definition，占比 0.58%)】极为罕见的设计，体内拥有 4 个独立的分裂板块。您的能量运作高度多层级，需要长久、有深度的长期关系与耐心独处来逐步对齐体内的多元能量。"
    else:
        def_analysis = "【无定义 / 反映者 (No Definition，占比 1.43%)】体内没有固定的通道连通。您的能量流完全由月亮过境周期（28.5天）及周遭环境采样决定，是社会的终极澄澈镜子。"

    bridge_details = []
    for b in bridge_channels:
        g1, g2 = b["gate_a"], b["gate_b"]
        c1_cn = CENTER_NAMES_CN.get(b["center_a"], b["center_a"])
        c2_cn = CENTER_NAMES_CN.get(b["center_b"], b["center_b"])
        
        if b["bridge_type"] == "Small Split Bridge":
            needed = b["needed_gate"]
            active_g = g1 if b["is_g1_active"] else g2
            bridge_details.append(
                f"✦ 【小桥接】{b['channel_name']}通道（{g1}-{g2}号）：连接【{c1_cn}】与【{c2_cn}】。您自身已激活 {active_g}号悬门，当遇到拥有 {needed}号卦门的人时，您会瞬间感到被'接通'的强烈吸引。"
            )
        else:
            bridge_details.append(
                f"✦ 【大桥接】{b['channel_name']}通道（{g1}-{g2}号）：连接【{c1_cn}】与【{c2_cn}】。需要完整的双卦门通道才能跨越该断裂区。"
            )

    if not bridge_details:
        bridge_details.append("✦ 能量连通闭合：您的定义中心已完整连通，不存在跨板块桥接断裂盲区。")

    black_channels = [c for c in defined_channels if c["color"] == "Personality"]
    red_channels = [c for c in defined_channels if c["color"] == "Design"]
    both_channels = [c for c in defined_channels if c["color"] == "Both"]

    red_black_analysis = f"【红黑双重系统觉察】您拥有 {len(black_channels)} 条黑色显意识通道（心智清醒认同）、{len(red_channels)} 条红色潜意识通道（身体遗传自动运转）以及 {len(both_channels)} 条红黑重合通道。"
    if red_channels:
        red_black_analysis += f" 值得注意的是，您的红色通道（如：{', '.join([c['name'] for c in red_channels])}）代表身体在切实行力，但您的头脑常后知后觉，需要建立更深的身体感觉觉察。"

    deconditioning_playbook = "【能量桥接去制约指南】1. 识别桥接制约：当您对某人产生强烈的依赖或“非他不可”的执念时，意识到这只是对方的卦门桥接了您的能量断裂区；2. 区分借用与本真：对方带给您的“完整感”是暂时的能量借用，离开对方后请回归自身的策略与内在权威；3. 享受连接而不执着：带着觉察去体验桥接带来的火花，不再将他人的能量误认为是自己。"

    return {
        "definition_type_cn": def_analysis,
        "subgraph_count": subgraph_count,
        "components_names": comp_names,
        "bridge_details": bridge_details,
        "hanging_gates_count": len(hanging_gates),
        "hanging_gates": hanging_gates,
        "red_black_analysis": red_black_analysis,
        "deconditioning_playbook": deconditioning_playbook
    }


from app.core.mandala import longitude_to_gate_line, longitude_to_substructure


def calculate_color_tone(longitude_deg: float) -> Tuple[int, int]:
    sub = longitude_to_substructure(longitude_deg)
    return sub["color"], sub["tone"]


def calculate_phs_and_variables(pers_lons: dict, des_lons: dict) -> dict:
    des_sun_sub = longitude_to_substructure(des_lons["Sun"])
    des_node_sub = longitude_to_substructure(des_lons["North_Node"])
    pers_sun_sub = longitude_to_substructure(pers_lons["Sun"])
    pers_node_sub = longitude_to_substructure(pers_lons["North_Node"])

    des_sun_color, des_sun_tone = des_sun_sub["color"], des_sun_sub["tone"]
    des_node_color, des_node_tone = des_node_sub["color"], des_node_sub["tone"]
    pers_sun_color, pers_sun_tone = pers_sun_sub["color"], pers_sun_sub["tone"]
    pers_node_color, pers_node_tone = pers_node_sub["color"], pers_node_sub["tone"]

    p1_letter = "L" if pers_sun_tone <= 3 else "R"
    p2_letter = "L" if pers_node_tone <= 3 else "R"
    d1_letter = "L" if des_sun_tone <= 3 else "R"
    d2_letter = "L" if des_node_tone <= 3 else "R"

    variable_code = f"P{p1_letter}{p2_letter}-D{d1_letter}{d2_letter}"

    var_body = "主动型的身体 (Left Active)" if des_sun_tone <= 3 else "被动型的身体 (Right Receptive)"
    var_brain = "主动思考/逻辑脑 (Left Active)" if pers_sun_tone <= 3 else "被动接收/右脑 (Right Receptive)"
    var_env = "观察型环境 (Left Observer)" if des_node_tone <= 3 else "观察型被动环境 (Right Receptive)"
    var_view = "聚焦型视角 (Left Focused)" if pers_node_tone <= 3 else "全局周边视角 (Right Peripheral)"

    digestion_info = PHS_DIGESTION_TYPES.get(des_sun_color, {"name_cn": "自由进食模式", "desc_cn": "顺应身体感受进食"})
    environment_info = PHS_ENVIRONMENT_TYPES.get(des_node_color, {"name_cn": "自然环境", "desc_cn": "舒适自然的空间"})
    perspective_info = PHS_PERSPECTIVE_TYPES.get(pers_node_color, {"name_cn": "独特视角", "desc_cn": "观察世界的方式"})
    motivation_info = PHS_MOTIVATION_TYPES.get(pers_sun_color, {"name_cn": "内在驱动", "desc_cn": "深层行为动机"})

    phs_deconditioning = "【身体去制约与线粒体活力恢复建议】请摒弃社会流行但并不适合您的固化饮食习惯。当您听从身体固有 Color 消化律与物理 Environment 居住环境时，您的肠道菌群与细胞线粒体会释放出令人惊叹的自愈活力。"
    phs_schedule = "【专属 PHS 高维养生日程表】早晨醒来避免立即进食过度复杂的混合食物；午间置身于符合您环境色彩的空间中；夜间保持环境平静，顺应您的 Tone 潜意识调养。"

    variable_desc = f"【{variable_code} 5重多维亚爻图层配置】"
    if "RR" in variable_code:
        variable_desc += "这是一种高度接收式的右脑认知设计。拥有此类配置的人，天生并不适合以传统的方式'主动死记硬背与过度计划'。你的身体和大脑都是为接收与全然在场而生。"
    else:
        variable_desc += "这是一种具备结构化与主动战略导向的认知设计，擅长通过清晰逻辑、计划与聚焦去探索和建构世界。"

    var_brain_deep = "【大脑认知模式 (P1 Brain Arrow)】" + ("您拥有定焦且擅长逻辑归纳的主动脑，适合结构化输出与清晰规划。" if p1_letter == 'L' else "您拥有海绵般强大吸收力的右脑，无需死板记忆，只需放松吸收，信息自然会在需要时浮现。")
    var_body_deep = "【身体防卫与代谢 (D1 Body Arrow)】" + ("您的身体需要通过有规律的运动与主动代谢来维持活力。" if d1_letter == 'L' else "您的身体需要放松、顺应自然的舒适节奏，避免过度剧烈的强迫性运动。")
    var_env_deep = "【环境观察与视角模式 (P2 & D2 Nodes)】" + ("您擅长从局部细节中精准捕捉焦点。" if p2_letter == 'L' else "您拥有全局周边视角，能宏观感知整体氛围与潜在机会。")

    return {
        "variable_code": variable_code,
        "variable_desc": variable_desc,
        "var_brain_deep": var_brain_deep,
        "var_body_deep": var_body_deep,
        "var_env_deep": var_env_deep,
        "phs_digestion": {
            "color": des_sun_color, "tone": des_sun_tone,
            "name_cn": digestion_info["name_cn"], "desc_cn": digestion_info["desc_cn"]
        },
        "phs_environment": {
            "color": des_node_color, "tone": des_node_tone,
            "name_cn": environment_info["name_cn"], "desc_cn": environment_info["desc_cn"]
        },
        "phs_perspective": {
            "color": pers_node_color, "tone": pers_node_tone,
            "name_cn": perspective_info["name_cn"], "desc_cn": perspective_info["desc_cn"]
        },
        "phs_motivation": {
            "color": pers_sun_color, "tone": pers_sun_tone,
            "name_cn": motivation_info["name_cn"], "desc_cn": motivation_info["desc_cn"]
        },
        "phs_deconditioning": phs_deconditioning,
        "phs_schedule": phs_schedule,
        "variables": {
            "body_arrow": var_body,
            "brain_arrow": var_brain,
            "environment_arrow": var_env,
            "view_arrow": var_view
        }
    }


def get_gene_keys_data(active_gates: list) -> list:
    gk_list = []
    for g in active_gates:
        gk_info = GENE_KEYS_SAMPLE.get(g, {
            "shadow": f"{g}号阴影 (Shadow)",
            "gift": f"{g}号天赋 (Gift)",
            "siddhi": f"{g}号悉地 (Siddhi)"
        })
        gk_list.append({
            "gate": g,
            "shadow": gk_info["shadow"],
            "gift": gk_info["gift"],
            "siddhi": gk_info["siddhi"],
            "shadow_desc": f"【阴影能级】在受挫时容易陷入{gk_info['shadow']}的低频自我防卫或焦虑中。",
            "gift_desc": f"【天赋能级】通过觉察将阴影转化为{gk_info['gift']}的强大现实创造力与解决问题能力。",
            "siddhi_desc": f"【悉地能级】最终升华为{gk_info['siddhi']}的高维灵性成就与无条件大爱。"
        })
    return gk_list


def get_bg5_business_strengths(defined_centers: list, defined_channels: list) -> dict:
    strengths = []
    if "Throat" in defined_centers:
        strengths.append("公关表达与品牌观点显化力 (Public Relations & Brand Manifestation)")
    if "Heart" in defined_centers:
        strengths.append("商业谈判、定价权与资源掌控力 (Commercial Negotiation & Resource Control)")
    if "Sacral" in defined_centers:
        strengths.append("持续项目建造、产品交付与运营力 (Product Operations & Building)")
    if "G_Center" in defined_centers:
        strengths.append("企业战略定位、品牌方向与文化引领力 (Corporate Strategy & Branding)")
    if "Solar_Plexus" in defined_centers:
        strengths.append("市场共情、情绪感染与客户关系维护 (Market Empathy & PR)")
    if "Spleen" in defined_centers:
        strengths.append("商业风控、质量把控与危机处理 (Risk Control & Quality Audit)")

    role = "商业架构师与高能执行者" if "Sacral" in defined_centers else "商业顾问、战略掌舵人与洞察官"

    wealth_strategy = "【商业变现防守与避坑策略】避免在未定义的中心盲目追求不属于自己的商业竞争。聚焦于您定义的中心与通道，活出天然商业优势是财富自然流动的秘密。"
    cooperation_model = "【最佳商业合作与雇佣模式】适合以独资合伙人、核心专家顾问或项目主导者的身份参与商业合作，保持决策的自主权。"
    wealth_action = "【商业变现落地行动 3 步走】1. 定位：明确您的核心商业角色；2. 定标：找准能与您优势互补的团队；3. 定价：基于您的心中心/喉咙中心优势坚定商业价值。"

    return {
        "business_role": role,
        "strengths_list": strengths,
        "wealth_strategy": wealth_strategy,
        "cooperation_model": cooperation_model,
        "wealth_action": wealth_action
    }


def get_psychological_traits(defined_centers: list, undefined_centers: list, variable_code: str) -> dict:
    traits = []
    if "Ajna" in defined_centers:
        traits.append({"topic": "思维范式", "desc": "您拥有极其稳定且定焦的逻辑架构。在思考问题时，您习惯以严谨的解构能力梳理脉络。请对自己温柔一些，无需为偶然的固执自责，这是您天然的理性锚点。"})
    else:
        traits.append({"topic": "思维范式", "desc": "您拥有天高云淡般开放灵动的多视角思考力。您的头脑是一座没有围墙的智慧图书馆，无需强迫自己死板固守某种特定观念，拥抱无限可能是您最大的天赋。"})

    if "Solar_Plexus" in defined_centers:
        traits.append({"topic": "情绪心理", "desc": "您的体内流动着丰富而深沉的情绪浪潮。在面对重要人生时刻时，请给予自己充足的时间与耐心，静待情绪波浪归于平静，澄澈的智慧自会浮现。"})
    else:
        traits.append({"topic": "情绪心理", "desc": "您对周遭的情绪氛围拥有水晶般透明的敏锐感知。您能深刻共情他人的喜怒哀乐，但请温柔地提醒自己：那些情绪风暴属于外界，不属于您自己。"})

    if "Head" in defined_centers:
        traits.append({"topic": "灵感与压力", "desc": "您的脑海中常年闪耀着丰沛的灵感火花。当思想压力袭来时，试着将它们化为创作与探索的动能，而非困扰睡眠的锁链。"})
    else:
        traits.append({"topic": "灵感与压力", "desc": "您的灵感如清风般自由，随时能被周遭的人与世界所点燃。学会辨别哪些问题值得关注，放掉那些不属于您的头脑焦虑。"})

    defense_mechanism = "【心理防卫机制破局】在面对外在不确定性时，学会识别自己是进入了'过度控制'还是'过度逃避'状态。通过观察而非批判，重建内在笃定的安全感。"
    self_healing = "【心理健康自愈与正念觉察】每日保留 15 分钟独处时光，练习观照呼吸。允许情绪像云彩般流过，重新回到内心安静澄明的心流状态。"

    cognition = "右脑海绵接收型认知（放松且全然在场）" if "PR" in variable_code or "RR" in variable_code else "主动逻辑型战略认知（定焦与结构化）"
    return {
        "cognition_style": cognition,
        "traits_list": traits,
        "defense_mechanism": defense_mechanism,
        "self_healing": self_healing
    }


def get_dream_rave_data(active_gates: list) -> dict:
    dream_gates_all = [19, 62, 50, 20, 57, 8, 1, 14, 5, 27, 48, 55, 30]
    activated_dream = [g for g in active_gates if g in dream_gates_all]

    light_gates = [g for g in active_gates if g in [62, 20, 8, 1]]
    demon_gates = [g for g in active_gates if g in [19, 50, 57, 48, 55, 30]]

    if len(light_gates) > len(demon_gates) and len(light_gates) > 0:
        realm_name = "✨ 光之领域 · 灵性飞翔与创造力梦境 (Light Realm)"
        realm_desc = "在睡眠中，您的意识倾向于上升至高频的【光之领域】。您常梦见开阔天空、飞翔、未解灵光的顿悟、或者充满艺术美感的场景。这是您的潜意识在吸收宇宙灵感火花。"
    elif len(demon_gates) > 0:
        realm_name = "🛡️ 阴影/恶魔领域 · 潜意识压力释放与情绪净化 (Demon Realm)"
        realm_desc = "在睡眠中，您的潜意识会进入【阴影领域】释放白天被压抑的生存焦虑。您可能会梦见被追赶、紧迫的时限、失控的场景或人际冲突。请不必惊慌，这是身体在夜间主动清理心智垃圾、释放情绪毒素的神圣自我保护机制。"
    else:
        realm_name = "🌿 大地/动物领域 · 物理细胞重塑与深度修养 (Earth Realm)"
        realm_desc = "您的睡眠属于极佳的【大地生理修养模式】。梦境往往与自然景色、动物、生活细节或平静的游走有关。您的物理身体在睡眠中能高效进行细胞级别的线粒体充能。"

    gate_analyses = []
    for g in activated_dream:
        if g == 19:
            gate_analyses.append("✦ 19号梦图卦门（依赖与空间需求）：夜间对睡眠环境的安全感要求极高，睡前需要被子包裹感与温暖氛围。")
        elif g == 57:
            gate_analyses.append("✦ 57号梦图卦门（直觉感知）：听觉在夜间高度敏感，微小的声音异响容易打断睡眠，建议使用隔音耳塞。")
        elif g == 50:
            gate_analyses.append("✦ 50号梦图卦门（责任与羁绊）：容易在梦中处理对家庭、团队或亲友的责任重担，醒来常伴有沉重感。")
        elif g == 62:
            gate_analyses.append("✦ 62号梦图卦门（细节点化）：梦境非常清晰且富有逻辑细节，醒来常能精准回忆起梦中的对话与画面。")
        elif g == 1:
            gate_analyses.append("✦ 1号梦图卦门（原始创造力）：潜意识在夜间重构审美与灵感，醒来第一分钟常有破局的新灵感。")
        elif g == 5:
            gate_analyses.append("✦ 5号梦图卦门（自然节律）：极度依赖固定的入睡与醒来时间表，规律作息能让您的精力恢复翻倍。")

    if not gate_analyses:
        gate_analyses.append("✦ 开放梦图神符通道：您的潜意识不受特定梦图卦门束缚，能随夜间天体过境自由吸收多元能量。")

    shadow_transformation = "当您梦见焦虑或被追赶时，醒来后请做 3 次深呼吸，对自己说：'这只是昨夜身体排出的心理积压，现实中的我是安全且充满力量的。'"
    sleep_physics = "【极度重要的磁场独立建议】在人类图梦图体系中，人处于睡眠无意识状态时，能量场会完全开放。如果您与他人同床或同室睡眠，您的电荷系统会强行吸收对方的能量印记，导致醒来后感到莫名疲惫。条件允许时，每周尝试 1-2 晚独立睡眠，您的身体将在极具安全感的个人磁场中获得脱胎换骨般的能量充能。"
    dream_journal = "【梦境灵感捕捉法】在床头准备一本灵感笔记本。醒来后的前 60 秒不要急于看手机或起床，保持身体不动，静静回味残留的梦境片段并快速记录，您将捕获潜意识赠予您的珍贵人生解答。"

    return {
        "dream_realm": realm_name,
        "realm_desc": realm_desc,
        "activated_dream_gates": activated_dream,
        "gate_analyses": gate_analyses,
        "shadow_transformation": shadow_transformation,
        "sleep_physics": sleep_physics,
        "dream_journal": dream_journal
    }


def get_love_and_relationships_data(active_gates: list) -> dict:
    love_active = []
    for g in active_gates:
        if g in GATES_OF_LOVE:
            love_active.append(GATES_OF_LOVE[g])

    if not love_active:
        love_active.append(GATES_OF_LOVE[10])

    love_magnetism = "✨ 宇宙无条件爱与尊严辐射 (Universal Love & Self-Grace)" if any(g in active_gates for g in [10, 25]) else "🌸 灵魂共鸣与深情陪伴 (Soul Resonance & Intimate Connection)"
    magnetism_desc = "在亲密关系中，您的磁场散发着温暖而真挚的能量。您不轻易开启心扉，但一旦确认了彼此的同频与真诚，您将奉献出极其深厚且富有包容力的爱。"
    electromagnetic_physics = "【合盘电磁吸引力法则】在人类图合盘中，当您与伴侣分别持有同一条通道的两个端点卦门时（例如您持有 10号自爱卦门，对方持有 20号临在卦门），就会在两人接触的瞬间触发强大的【电磁连通通道】。这种火花带来了强烈的化学吸引力，是灵魂深深相互吸引的物理印记。"
    love_shadow = "【爱中的非自我防御陷阱】在关系深处，请警惕'讨好型防御'或'过度牺牲自我的迎合'。当您害怕失去伴侣时，头脑可能会逼迫您委曲求全。请记住：真正的爱从来不需要以牺牲个人尊严为代价，保持独立的自我才是吸引持久真爱的终极秘密。"
    love_communication = "【亲密关系沟通与边界法则】请根据您的内在权威去沟通情感表达。当您感到关系中有情绪波浪时，不要在冲动下做绝对性的承诺或决裂。给予彼此充裕的思考空间，在澄澈和平静中说出的爱，才最具穿透力。"

    return {
        "love_theme": love_magnetism,
        "magnetism_desc": magnetism_desc,
        "active_love_gates": love_active,
        "electromagnetic_physics": electromagnetic_physics,
        "love_shadow": love_shadow,
        "love_communication": love_communication
    }


def get_penta_team_capabilities(active_gates: list, defined_centers: list) -> dict:
    penta_gates = [15, 5, 2, 14, 46, 29, 8, 1, 31, 7, 33, 13]
    active_penta = [g for g in active_gates if g in penta_gates]

    roles = []
    if any(g in active_penta for g in [31, 7]):
        roles.append("团队战略领袖与指引者 (Visionary Leader)")
    if any(g in active_penta for g in [2, 14]):
        roles.append("资源配置与商业掌舵人 (Resource Master)")
    if any(g in active_penta for g in [46, 29]):
        roles.append("项目落地与高能量执行者 (Execution Powerhouse)")
    if any(g in active_penta for g in [8, 1]):
        roles.append("品牌对外公关与文化建设者 (Brand Ambassador)")

    if not roles:
        roles.append("独立顾问与核心专家 (Independent Specialist)")

    penta_shortage = "【团队能量短板与补位策略】若您的 Penta 12 柱石卦门未完全覆盖，在 3~5 人小团队中容易出现某个环节（如资源或公关）空缺。建议引入拥有互补卦门的团队成员，实现无缝协同。"
    penta_defense = "【团队内耗防御指南】在 Penta 小团体中，个人性格会被缩小，团队生态位会被放大。明确各自的商业柱石职责，能避免权力重叠与无谓的内耗摩擦。"
    penta_building = "【高效 3-5 人精英团队协同法则】打造极致协同团队的秘诀在于：让领袖做战略，让资源官掌管预算，让执行官聚焦落地，让公关大使面向市场。"

    return {
        "penta_role": roles[0],
        "all_roles": roles,
        "active_penta_gates": active_penta,
        "penta_shortage": penta_shortage,
        "penta_defense": penta_defense,
        "penta_building": penta_building
    }
