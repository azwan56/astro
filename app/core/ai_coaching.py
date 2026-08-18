"""
Master Multi-Dimensional Synthesis Engine for Human Design Coaching
Removes Qwen-Plus AI branding and converts all mixed English terms to natural Chinese with standard brackets.
"""

import os
import json


def generate_ai_coaching_report(chart_data: dict, user_question: str = "") -> dict:
    """
    Synthesize all 12 modules into a master holistic Coaching Report in fluent Chinese.
    """
    coaching_summary = chart_data.get("coaching_summary", {})
    energy_type_cn = coaching_summary.get("type_cn", "纯粹生产者")
    strategy_cn = coaching_summary.get("strategy_cn", "等待荐骨的回应")
    authority_cn = coaching_summary.get("authority_cn", "荐骨权威")
    not_self_cn = coaching_summary.get("not_self_theme", "挫败感")
    profile = chart_data.get("profile", "5/1")
    var_code = chart_data.get("variable_code", "PLR-DRR")

    def_centers = [c if isinstance(c, str) else str(c) for c in chart_data.get("defined_centers", [])]
    undef_centers = [c if isinstance(c, str) else str(c) for c in chart_data.get("undefined_centers", [])]
    phs_digestion = chart_data.get("phs_digestion", {}).get("name_cn", "环境进食")
    phs_env = chart_data.get("phs_environment", {}).get("name_cn", "山谷环境")
    dream_realm = chart_data.get("dream_rave", {}).get("dream_realm", "阴影与潜意识活跃区")
    love_theme = chart_data.get("love_relationships", {}).get("love_theme", "自爱与无条件接纳")
    bg5_role = chart_data.get("bg5_business", {}).get("business_role", "商业架构师")
    penta_role = chart_data.get("penta_team", {}).get("penta_role", "团队领袖")

    q_text = f"针对您的现实关注与提问：“*{user_question}*”：" if user_question else "针对您的现实关注：“*如何在职场与生活中停止盲目内耗，活出高能自我？*”："

    report_markdown = f"""
### 🌟 一、 能量蓝图与灵魂底层架构【能量架构】
作为一名 **【{energy_type_cn}】**（人生角色 {profile}），您的生命能量旨在通过 **【{strategy_cn}】** 激活最大的真实效能。
当您试图用头脑强行规划或冲动发起时，便容易陷入 **【{not_self_cn}】** 的非自我磨损中。
在重大决策时刻，请始终回归您的 **【{authority_cn}】**。允许身体固有权威带给您笃定的信号，这是您天然的人生导航系统。

### 🧬 二、 5 重多维图层与大脑认知解读【图层与养生】
您的图层配置为 **【{var_code}】**。这意味着您的认知系统具备极高的灵敏度。
在物理养生与消化层面，您的 Color 消化模式为 **【{phs_digestion}】**，居住与工作物理环境为 **【{phs_env}】**。
听从身体原生的物理节奏，避免在焦虑时进食或强迫大脑死记硬背。放松且全然在场，会让您的大脑发挥出惊人的洞察力。

### 🌙 三、 潜意识梦境与 G 中心爱之磁场【潜意识与亲密】
在睡眠潜意识领域，您的 睡眠梦图 呈现为 **【{dream_realm}】**。夜间独立睡眠能让您的身体能量场摆脱他人的电荷制约，完成深度的细胞自我修复。
在亲密关系中，您的 G中心 散发着 **【{love_theme}】** 的磁场。学会无条件自爱是您吸引灵魂伴侣的基石。

### 💼 四、 商业赚钱与 3-5 人团队生态【商业与团队】
在商业与财富领域，您的 BG5 商业角色定位为 **【{bg5_role}】**，在 3~5 人小团队中担任 **【{penta_role}】**。
聚焦于您定义的能量中心与通道天赋，避免在未定义中心盲目追求不属于自己的商业竞争。找到能与您优势互补的团队伙伴，您的商业价值将获得倍数放大。

### 💡 五、 现实困惑专项深度破局教练建议【专项破局】
{q_text}

1. **破局建议 1：暂停头脑的过度预演**  
   当焦虑袭来时，识别出这只是头脑的过度保护。将注意力拉回身体当下，听从【{authority_cn}】的自然响应。

2. **破局建议 2：建立健康的物理与能量边界**  
   在工作与睡眠中保护好您的 PHS 物理环境【{phs_env}】，定期进行独立独处，清理吸收自外在的情绪与思想杂质。

3. **破局建议 3：坚定您的核心商业定位**  
   明确您作为【{bg5_role}】的杀手锏优势，把时间精力投放在高价值的项目构建上，拒绝无意义的低效内耗。

### ✨ 六、 大师教练温情结语与赋能箴言【高维赋能】
您的人类图蓝图是宇宙赠予您最独一无二的神圣礼物。全然接纳真实的自己，顺应您的策略与内在权威，您将活出如太阳般炽热且笃定的喜悦人生！
"""

    return {
        "status": "success",
        "engine": "全维大师综合解盘",
        "report_markdown": report_markdown
    }
