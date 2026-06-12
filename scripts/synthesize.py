"""Synthesize 20 narration audio files using edge-tts.

Rhythm control via standard Chinese punctuation (Azure TTS handles these reliably):
  ， = short pause  —— = longer pause  。 = full stop
  、 = enumeration  换行/分段 = natural break between segments
NO SSML, NO ... or —— (TTS reads them as text or creates unpredictable pauses).
Use Communicate's built-in rate parameter for pacing.
"""

import asyncio
import edge_tts
import os

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio")
VOICE = "zh-CN-YunyangNeural"

NARRATIONS = [
    # Step 0: Hook — casual opening
    "张自祺，投券商AI技术服务岗。这份简历我们逐条拆一遍，看改了什么，为什么这样改。",

    # Step 1: Golden sentence — core idea
    "整份简历围绕一句话改：别写你做过什么，写你能帮对方做什么。",

    # Step 2: Three problems intro
    "先看看原来的简历有什么问题。",

    # Step 3: Problem 1 — no profile, three-second death
    "没写专业概要。HR打开前三秒看不到你是谁，投什么岗，直接关。",

    # Step 4: Problem 2 — scattered skills
    "技能撒在各段经历里，像夹在菜里的配料。HR没空帮你挑出来归类。",

    # Step 5: Problem 3 — weak verbs, no deliverables
    "每条都是负责什么，参与什么。干了啥写了，干出了啥没写。",

    # Step 6: Strategy — three directions
    "这个岗的JD要看AI视频，IP营销，引流开户。那我们就把所有经历往三个方向靠：内容生产，自动化，交付速度。",

    # Step 7: Fix 1 — added profile summary
    "第一处改了这里：加了一段专业概要。四句话。你有什么能力，拿什么工具干活，跨专业背景怎么变成你的优势，最后落到你能帮业务解决什么问题。",

    # Step 8: Fix 2 — skills matrix
    "第二处：把散在各段的技能抽出来，拼成六列矩阵。AI开发，智能体，AIGC，自动化，知识管理，办公协作。一眼看完。",

    # Step 9: Fix 2 — before/after example
    "看例子。原文：熟练使用AI工具制作视频。改成：搭建AIGC内容生产线，覆盖从制作到多平台分发的完整链路。不写会用工具，写用工具搭了什么。",

    # Step 10: Fix 3 — verb upgrade
    "第三处：动词。原文写掌握智能体任务分发。掌握，是说你自己的状态。改成设计任务分发与工作流编排，实现复杂任务自动化协同。这才是说你做了什么。",

    # Step 11: Fix 4 — add deliverables
    "第四处：每条经历后面补产出物。原来写测评学术AI工具，改后加了一句：输出功能对比评估报告，为采购决策提供依据。补一句，就知道这事你真的做了。",

    # Step 12: Additional fixes — same pattern applied
    "其余几段同理。盛喜工效七条合为四条，把审批流，人事管理，资产台账这些模块名写进去。火车站补了跨部门协调。东曜药业那段留了GMP合规，券商是强监管，这个关键词有用。",

    # Step 13: Review — what changed
    "过一遍改了什么：加了概要。技能收成矩阵。动词换掉。补了产出。跨专业没藏，反过来说这让你学东西更快。合规经验用来侧面呼应券商。",

    # Step 14: Hard truth 1 — cross-disciplinary background
    "有两个点，面试大概率会被问。第一个：你学食品和公共管理的，为什么来做AI。",

    # Step 15: Hard truth 2 — zero finance background
    "第二个：简历里没有金融相关内容。有自学就补一行。没有的话，至少搞清楚券商靠什么赚钱，以及内容合规的底线在哪里。",

    # Step 16: Resolution — don't hide weaknesses
    "这两个短板躲不掉，不用躲。承认它，说你在补，再说你的背景能给团队带来什么不一样的东西。",

    # Step 17: Four pillars — the core logic
    "这份简历的改法就四件事。写你能帮对方做什么，不写你做过什么。写体系，不列工具清单。短板不藏，准备好怎么回答。每句话都有出处。",

    # Step 18: CTA — supplement guide
    "补充指导文档里有每条修改的三列对照：原文，优化后，理由。改你自己的时候对着看就行。",

    # Step 19: Final frame — landing
    "拆完了。改简历改的不是措辞，是对方怎么看你的方式。",
]


async def synthesize_one(idx: int, text: str) -> str:
    out_path = os.path.join(OUT_DIR, f"{idx:02d}.mp3")
    if os.path.exists(out_path):
        print(f"  [{idx:02d}] 已存在，跳过")
        return out_path
    communicate = edge_tts.Communicate(text, VOICE, rate="+5%")
    await communicate.save(out_path)
    print(f"  [{idx:02d}] → {out_path}")
    return out_path


async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print(f"Voice: {VOICE}")
    print(f"Total segments: {len(NARRATIONS)}")
    print(f"Output: {OUT_DIR}\n")

    tasks = [synthesize_one(i, text) for i, text in enumerate(NARRATIONS)]
    await asyncio.gather(*tasks)

    print(f"\nDone! {len(NARRATIONS)} audio files in {OUT_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
