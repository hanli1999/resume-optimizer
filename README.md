# 五维三轴简历优化引擎 · Resume Optimizer

> 输入一份简历（PDF/DOCX），输出 3 个 PDF。全流程 6-7 阶段。
> 核心原则：**可优化表达，不生成虚假信息。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)
![Templates: 6](https://img.shields.io/badge/Templates-6-blue)

## 这是什么

一个 **Claude Code Skill**。放在 `~/.claude/skills/` 目录下，对 Claude 说"帮我优化这份简历"即自动运行全流程。

如果你不用 Claude Code，skill 里的 Python 脚本和 HTML 模板也可以独立使用——手动跑提取、排版、导出 PDF。

输入你的简历 PDF 或 DOCX，AI 自动：

1. 提取文本和照片
2. 用"五维三轴"框架做结构化分析（行业背景、岗位经验、技能等级、地理位置、个性特质 + 身份轴/需求轴/条件轴）
3. 6 种专业排版模板智能选择（根据行业、内容密度、职级自动匹配）
4. 优化表达措辞，重组内容结构
5. **真实性审计**——逐句比对原文，标记所有差异，禁止虚构信息
6. 输出 3 个 PDF：双页详细版 + 单页浓缩版 + 补充指导文档

可选：提供岗位 JD，启用岗位匹配模式——在真实信息范围内向岗位要求靠拢（绝不虚构技能/证书/项目）。

## 为什么开源

这是 幻梦 为 银月自主运行系统 开发的辅助工具。原本是内部使用的 Claude Code Skill。

开源是因为：**AI 帮你写简历不难，难的是"不编"。** 市面上大多数 AI 简历工具会帮你凭空生成"精通 Python""主导过百万用户项目"——这个不会。

所有优化可追溯至原文。所有差异标注级别。所有不确定性诚实告知。

## 输出物（3个PDF + 可选视频）

| # | 文件 | 用途 |
|---|------|------|
| PDF 1 | 双页优化简历 | A4双页，适合邮件投递/仔细阅读 |
| PDF 2 | 单页浓缩简历 | 单页A4，适合打印/招聘会 |
| PDF 3 | 补充指导文档 | 需确认项+修订对照表+岗位匹配分析 |
| 可选 | 视频讲解网页 | 1920×1080 自播放网页，逐帧标注修改点，配合口播旁白。打开即看，可录屏分享 |

## 快速开始

### 作为 Claude Code Skill 使用

将整个文件夹复制到你的 skills 目录：

```bash
# Claude Code
cp -r resume-optimizer ~/.claude/skills/

# 在对话中说
"帮我优化这份简历"
```

### 独立使用 Python 脚本

```bash
pip install pdfplumber python-docx playwright Pillow
python -m playwright install chromium

# 按 SKILL.md 中的 Phase 0 → Phase 5 流程运行
```

## 文件结构

```
resume-optimizer/
├── README.md                # 完整文档
├── LICENSE                  # MIT
├── scripts/
│   └── synthesize.py        # 合成脚本
└── templates/
    ├── resume-two-page*.html  # 6 套双页模板 (A-F)
    ├── resume-one-page*.html  # 6 套单页模板 (A-F)
    ├── supplement-guide.html  # 补充指导模板
    └── presentation.html      # 模板展示文档
```

## 模板预览

| A — 深色侧边栏 | B — 顶部通栏 | C — 经典居中 |
|:---:|:---:|:---:|
| 海军蓝 + 蓝 | 青绿 | 深蓝 + 金 |
| 技术/工程岗 | 管理/综合岗 | 资深/高管 |

| D — 现代杂志 | E — 极简线条 | F — 醒目分割 |
|:---:|:---:|:---:|
| 黑 + 橙 | 靛蓝 | 紫色渐变 |
| 年轻/跨领域 | 阅读型/简洁 | 关键指标突出 |

## 五维三轴框架

**五维（能力基本面）：** 行业背景、岗位经验、技能等级、地理位置、个性特质

**三轴（供需匹配）：** 身份轴（年限/证书/年龄）、需求轴（薪资/班次/福利）、条件轴（加班/环境/用工形式）

## 铁律

- 不凭空生成技能、证书、项目经历
- 不添加候选人不会的设备/软件名
- 不虚构量化数据
- 不调整学历信息
- 所有优化可追溯至原文出处
- 永远先审计再输出

## 许可证

MIT License — 随意使用、修改、分发。

## 作者

幻梦 + 银月（SilverMoon Project）
基于 Claude Code Skill 架构

---
---
name: resume-optimizer
description: 五维三轴简历优化引擎。输入简历PDF/DOCX（可选JD），输出3个PDF：双页优化简历、单页浓缩简历、补充指导文档。核心流程：提取→五维三轴分析→（可选：岗位匹配）→表达优化→真实性审计→HTML生成→PDF导出。不凭空生成虚假信息，所有优化可追溯至原文。默认不结合岗位要求，用户提供JD时才启用岗位匹配模式。
metadata:
  type: skill
---

# 五维三轴简历优化引擎（Resume Optimizer）

输入一份简历（PDF/DOCX），输出 3 个 PDF 文件。全流程 6-7 阶段，核心原则：**可优化表达，不生成虚假信息**。

## 两种运行模式

### 模式 1：纯简历优化（默认）
用户只提供简历，不提供岗位 JD。流程跳过 Phase 1.5（岗位匹配），仅优化简历表达和排版。

### 模式 2：岗位匹配优化（用户提供 JD 时启用）
用户同时提供简历 + 岗位 JD 时启用。在五维分析后增加岗位匹配分析，优化时在真实信息范围内向岗位要求靠拢。

**触发条件：** 用户在投递简历时明确说"这个岗位的要求是……""帮我针对这个JD优化""这是岗位信息……"等。或直接提供了岗位链接/截图/文本。

**⚠️ 铁律：即使在岗位匹配模式下，也绝不凭空生成技能、证书、项目经历。只能调整表达的侧重点和关键词密度，让已有的真实经验更容易被 JD 关键词命中。**

## 输出物

| # | 文件 | 用途 |
|---|------|------|
| PDF 1 | `姓名_优化简历_客观版.pdf` | 双页 A4 排版，适合仔细阅读/邮件发送 |
| PDF 2 | `姓名_优化简历_单页版.pdf` | 浓缩至 1 张 A4，适合打印投递/招聘会 |
| PDF 3 | `姓名_简历补充指导.pdf` | 标注所有需候选人确认/补充的信息，含修订对照表。如启用岗位匹配模式，额外包含岗位匹配分析 |

---

## Complete Workflow (6-7 Phases)

```
Phase 0: 简历提取 → Phase 1: 五维三轴分析 → [Phase 1.5: 岗位匹配分析（仅JD模式）]
→ Phase 2: 内容优化 → Phase 3: 真实性审计 → Phase 4: HTML 生成 → Phase 5: PDF 导出
```

---

## Phase 0: 简历提取（Resume Extraction）

### 输入格式

- **PDF**：用 `pdfplumber` 提取文本 + 照片（如有嵌入图片）
- **DOCX**：用 `python-docx` 提取文本
- **纯文本/图片**：直接使用或 OCR

### 提取步骤

```bash
# 安装依赖
pip install pdfplumber python-docx -q

# 提取 PDF 文本
python -c "
import pdfplumber
with pdfplumber.open('简历.pdf') as pdf:
    for page in pdf.pages:
        print(page.extract_text())
"

# 提取 PDF 中的照片（如有）
python -c "
import pdfplumber
from PIL import Image
from io import BytesIO
with pdfplumber.open('简历.pdf') as pdf:
    for j, img in enumerate(pdf.pages[0].images):
        data = img['stream'].get_data()
        with open(f'photo_{j}.jpg', 'wb') as f:
            f.write(data)
        Image.open(BytesIO(data)).save(f'photo_{j}.png')
"
```

### 输出

一份完整的原始文本转写，保留所有原始数据（包括原文措辞、数字、日期）。

---

## Phase 1: 五维三轴分析（Framework Analysis）

用五维三轴框架对候选人进行结构化画像。

### 五维：能力基本面

| 维度 | 提取内容 | 标签数 |
|------|---------|--------|
| 1. 行业背景 | 候选人曾在哪些行业工作 | 通常 2-5 个 |
| 2. 岗位经验 | 具体做过哪些岗位/工种 | 每个岗位 1 个标签 |
| 3. 技能等级 | 硬技能深度与广度，含证书 | 通常 5-15 个 |
| 4. 地理位置 | 现居/期望城市、出差/驻厂/通勤偏好 | 5-7 个 |
| 5. 个性/特质 | 从经历描述中推断的软技能 | 3-5 个 |

### 三轴：供需匹配轴

| 轴 | 人才端标签 | 提取来源 |
|----|----------|---------|
| 身份轴 | 从业年限、持证情况、年龄 | 简历头部信息 |
| 需求轴 | 期望薪资、期望班次、期望福利、期望岗位 | 求职意向 |
| 条件轴 | 接受加班、接受工作环境、接受用工形式 | 自我评价/经历推断 |

**如果用户同时提供了 JD**，则同时做企业端五维三轴拆解并输出五维匹配度矩阵和三轴重合度表（见 Phase 1.5）。

**如果用户只提供简历无 JD**，则只做人才端画像，不输出匹配度。跳过 Phase 1.5。

---

## Phase 1.5: 岗位匹配分析（Job Match Analysis）⚠️ 仅 JD 模式

**此阶段仅在用户提供了岗位 JD 时执行。默认跳过。**

### 步骤 1: JD 关键词提取

从岗位 JD 中提取：

| 类别 | 提取内容 |
|------|---------|
| 硬技能要求 | 具体设备/软件/工具名称（如：西门子PLC、发那科机器人、EPLAN） |
| 证书要求 | 必备证书 + 加分证书（如：低压电工证、高压电工证） |
| 学历门槛 | 最低学历要求 |
| 经验年限 | 要求几年经验 |
| 关键词 | JD 中反复出现的动词和名词（如：故障诊断、预防性维护、TPM） |
| 软性要求 | 出差、倒班、沟通、团队合作等 |

### 步骤 2: 候选人匹配度分析

逐项比对候选人真实经历与 JD 要求：

| 匹配等级 | 含义 | 处理方式 |
|----------|------|---------|
| ✅ 直接匹配 | 候选人明确有该技能/经验 | 在简历中**高亮或前移**该信息 |
| 🟡 间接匹配 | 候选人有相关但不完全相同的经验 | 调整措辞使关键词更接近 JD 用语，但不虚构具体设备名 |
| ⚪ 无信息 | 候选人简历未提及此项 | **不做任何处理**，在补充指导中标注"JD 要求但简历未体现" |
| ❌ 不匹配 | 候选人明确不符合（如学历不够） | 在补充指导中诚实标注 |

### 步骤 3: 可优化清单

列出在真实性约束下可以做的事情：

1. **关键词对齐**：候选人的"全自动贴合机"如果 JD 写"自动化贴合设备"→ 改用 JD 用语
2. **侧重点调整**：JD 看重 PLC 则把 PLC 相关经验前移，JD 看重客户培训则突出培训经历
3. **叙事框架适配**：按 JD 的能力模型重组经历描述结构
4. **技能标签顺序重排**：把匹配度最高的技能放前面

### 严禁操作（铁律）

- ❌ 添加候选人不会的设备/软件名（即使 JD 要求）
- ❌ 添加候选人没有的证书（即使 JD 要求）
- ❌ 虚构项目经历或量化数据
- ❌ 调整学历信息
- ❌ 夸大经验年限

### 输出

五维匹配度矩阵 + 可优化清单 + 补充指导中增加"岗位匹配分析"章节。

---

## Phase 2: 内容优化（Content Optimization）

### 优化原则

1. **不添加原文没有的事实**：技能、项目、数据必须能在原文中找到出处
2. **可以重组和强化表达**：将散落的技能合并为矩阵、将长段落拆为 bullet point
3. **可以构建叙事框架**：如"设备维护→PLC编程→系统集成→技术管理"，但框架必须基于真实的职业轨迹
4. **数据加粗突出**：量化成果使用 `<strong>` 或特殊样式突出
5. **职业化措辞**：如"自己单干"→"独立执业"，但保留核心事实
6. **【仅 JD 模式】关键词对齐**：在不虚构的前提下，将候选人技能描述的用词向 JD 靠拢。例如 JD 写"预防性维护"而简历写"日常保养"，改用"预防性维护"。但 JD 要求的设备名称候选人确实不会的，不写。
7. **【仅 JD 模式】匹配项前移**：将与 JD 匹配度最高的技能/经历放在简历中更显眼的位置（概要首句、技术矩阵首列、经历首条 bullet）

### 简历结构设计

**四种模板布局可用，根据候选人画像智能选择。**

---

## 模板目录与选择规则（Template Catalog）

共 6 个模板系列，每个系列含双页版 + 单页版。**禁止默认使用模板 A**，每次都需根据候选人画像做选择。

### 模板速查表

| 模板 | 布局 | 色系 | 特征 | 最适用 |
|------|------|------|------|--------|
| **A** — 深色侧边栏 | 左深色竖栏(220px) + 右白 | 海军蓝 `#0f172a→#1e3a5f` + 蓝 `#2563eb` | 信息密度高，侧栏集中证书/标签/关键数据 | 技术/工程岗，证书多，设备/工具标签密集 |
| **B** — 顶部通栏 | 全宽深色Header + 下方双栏 | 青绿 `#0d9488→#115e59` | Header 展示姓名+联系方式，左下右窄 | 管理/综合岗，信息均衡，行业经验丰富 |
| **C** — 经典居中 | 居中姓名 + 单栏竖排 | 深蓝 `#1e3a5f` + 金 `#c4943b` | 庄重典雅，左侧金线强调，大量留白 | 传统行业，资深/高管，教育背景强的候选人 |
| **D** — 现代杂志 | 黑色通栏Banner + 三栏 | 黑 `#18181b` + 橙 `#f97316` | 现代大胆，Banner 展示 3 个关键数据 | 年轻候选人，跨领域，创意/新能源行业 |
| **E** — 极简线条 | 单栏，细线分割 | 靛蓝 `#6366f1` | 极简留白，圆形 bullet，淡色日期 | 阅读型简历，文字内容多，追求简洁专业感 |
| **F** — 醒目分割 | 紫色渐变顶块 + 白底双栏 | 紫色 `#7c3aed→#5b21b6` | 顶部彩色块展示姓名+关键数据，三角 bullet | 需要视觉冲击力，关键指标突出，证书标签多 |

### 选择规则（按优先级）

1. **行业匹配优先**：
   - 光伏/锂电/半导体/自动化 → **A** 或 **D** 或 **F**
   - 传统制造/建筑/物流 → **C** 或 **E**
   - 互联网/设计/营销 → **D** 或 **B**
   - 管理/项目经理/总监 → **B** 或 **C** 或 **E**

2. **内容密度匹配**：
   - 证书 ≥3 个 + 技能标签 ≥10 个 → **A**（侧栏最擅长承载密集标签）
   - 工作经历 ≤2 段，内容相对简单 → **C** 或 **E**（留白多显庄重）
   - 多段短期外包/项目制经历 → **B** 或 **D**（不用侧栏，主体空间大）
   - 技能跨领域、需要 3 列分类 → **D**（三栏天然匹配）
   - 关键指标突出（效率/成本/规模数字多）→ **F**（顶部统计块展示）

3. **经验与职级**：
   - 5 年以下 / 初级 → **D** 或 **F**（现代感强，视觉冲击弥补经验）
   - 5-10 年 / 中级 → **A** 或 **B** 或 **E**（信息密度和结构感最均衡）
   - 10 年以上 / 高级 → **C** 或 **E**（稳重传统，突出资历深度）

4. **轮换规则**：
   - 同一批次处理多份简历时，**至少使用 2 种不同模板**
   - 连续两单不要用同一模板（记忆上次使用的模板）
   - 默认轮换顺序：A → B → C → D → E → F → A（如不匹配候选人则跳过）

### 模板文件清单

| 模板 | 双页版 | 单页版 |
|------|--------|--------|
| A — 深色侧边栏 | `templates/resume-two-page.html` | `templates/resume-one-page.html` |
| B — 顶部通栏 | `templates/resume-two-page-b.html` | `templates/resume-one-page-b.html` |
| C — 经典居中 | `templates/resume-two-page-c.html` | `templates/resume-one-page-c.html` |
| D — 现代杂志 | `templates/resume-two-page-d.html` | `templates/resume-one-page-d.html` |
| E — 极简线条 | `templates/resume-two-page-e.html` | `templates/resume-one-page-e.html` |
| F — 醒目分割 | `templates/resume-two-page-f.html` | `templates/resume-one-page-f.html` | `templates/supplement-guide.html`，不随简历模板变化。

### 双页版 vs 单页版差异（所有模板通用）

| 特征 | 双页版 | 单页版 |
|------|--------|--------|
| 每段经历 bullet | 3-4 条 | 1-2 条 |
| 字号 | 13-14px 正文 | 11-12px 正文 |
| 间距 | 正常 | 紧凑 |
| 页面高度 | min-height: 1123px | height: 1123px + overflow:hidden |
| 适用场景 | 邮件/仔细阅读 | 打印投递/招聘会 |

---

## Phase 3: 真实性审计（Truth Audit）⚠️ CRITICAL

**这是本 skill 最关键的步骤。** 逐项比对优化版与原文，标记所有差异并分类：

### 审计分类

| 级别 | 含义 | 示例 |
|------|------|------|
| ✅ 完全匹配 | 优化版表述可直接在原文找到出处 | 数字、公司名、岗位名 |
| ⚠️ 措辞强化 | 原文基础上加强了表达力度 | "负责"→"主导"（如原文确实描述了主导行为） |
| 🔴 过度推断 | 添加了原文未明确支持的表述 | "听说良好"→"可全英文技术交流" |
| ❌ 凭空生成 | 新增了原文完全没有的信息 | 虚构项目、技能、证书 |

### 审计流程

1. 逐句比对优化版专业概要，确认每句话的出处
2. 逐个核对技能标签（8品牌PLC → 确认原文逐一列出）
3. 核对每个数字（年份、金额、速度、面积）
4. 核对证书和学历信息
5. 将所有 🔴 和 ❌ 项修正为 ✅ 或 ⚠️ 级别
6. 输出修正后的客观版简历

### 审计后必须修正的典型问题

- "8+" → "8大"（精确数不加号）
- "可全英文技术交流" → "英语读写及听说能力良好"（忠于原文措辞）
- "独立主导" → "主导"（原文未说"独立"）
- "显著减少" → "减少"（不加程度副词）
- "符合审计要求" → "符合行业规范"（不推断具体标准）
- 删除所有主观评分（如星级、能力雷达图的主观打分）

---

## Phase 4: HTML 生成（HTML Generation）

### 文件 1 & 2：优化简历 HTML

使用 `templates/resume-optimized.html` 模板结构。关键 CSS 参数：
- A4 尺寸：794px 宽
- 左栏深色渐变背景（`#0f172a → #1e3a5f`）
- 右栏白色，蓝色（`#2563eb`）分割线
- 打印友好：`@media print` 去除背景色

生成时注意：
- 照片引用本地路径（`photo_0.png`），与 HTML 同目录
- 所有字体使用中文字体栈：`"PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif`
- `@page { size: A4; margin: 0; }` 确保 PDF 输出正确

### 文件 3：补充指导 HTML

使用 `templates/supplement-guide.html` 模板结构。包含：
1. **汇总框**：需要补充/确认的事项数量
2. **必须确认项**（红色标记）：面试可能被质疑的硬伤
3. **建议补充项**（黄色标记）：提升竞争力的量化数据
4. **可选增强项**（蓝色标记）：锦上添花的内容
5. **【仅 JD 模式】岗位匹配分析**（新增章节）：五维匹配度矩阵 + 可优化清单 + JD 要求但简历未体现的技能/证书（诚实标注，供候选人自行决定是否补充）
6. **修订说明表**：原文→优化后→理由 三列对照
7. **下一步行动清单**：优先级排序的待办列表

---

## Phase 5: PDF 导出（PDF Export）

### 步骤

```bash
# 1. 启动本地 HTTP 服务器（供 Playwright 加载 HTML + 本地图片）
cd <简历目录> && python -m http.server 8765 &

# 2. 用 Playwright 渲染为 PDF
python -c "
from playwright.sync_api import sync_playwright
import os

os.chdir(r'<简历目录>')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # PDF 1: 双页客观版
    page.goto('http://localhost:8765/姓名_优化简历_客观版.html', wait_until='networkidle')
    page.pdf(path='姓名_优化简历_客观版.pdf', format='A4', print_background=True,
             margin={'top':'0','bottom':'0','left':'0','right':'0'})
    
    # PDF 2: 单页版
    page.goto('http://localhost:8765/姓名_优化简历_单页版.html', wait_until='networkidle')
    page.pdf(path='姓名_优化简历_单页版.pdf', format='A4', print_background=True,
             margin={'top':'0','bottom':'0','left':'0','right':'0'})
    
    # PDF 3: 补充指导
    page.goto('http://localhost:8765/姓名_简历补充指导.html', wait_until='networkidle')
    page.pdf(path='姓名_简历补充指导.pdf', format='A4', print_background=True,
             margin={'top':'0','bottom':'0','left':'0','right':'0'})
    
    browser.close()
    print('All 3 PDFs saved')
"
```

### 依赖清单

```bash
pip install pdfplumber python-docx playwright Pillow -q
python -m playwright install chromium  # 首次使用需要安装浏览器
```

### 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| 照片不显示 | HTML 引用路径不对 | 确认 `<img src="photo_0.png">` 与 HTML 同目录 |
| PDF 超出 A4 | 内容太多 | 先出双页版；如双页仍溢出，调整 font-size 和 padding |
| 中文乱码 | 字体栈缺中文字体 | 确保 CSS 有 `"Microsoft YaHei"` 或 `"PingFang SC"` |
| Playwright 报错 | 浏览器未安装 | `python -m playwright install chromium` |

---

## Quick Reference Card

```
简历提取:    pdfplumber / python-docx → 纯文本 + 照片 PNG
五维分析:    5维能力画像 + 3轴供需标签（无JD则只做人才端）
[可选]岗位匹配:  用户提供JD时启用 → JD关键词提取 → 匹配分析 → 可优化清单
模板选择:    根据行业/内容密度/职级选模板 A/B/C/D（禁止总是用 A）
内容优化:    套用选定模板；默认模式纯优化表达，JD模式额外做关键词对齐+匹配项前移
真实性审计:  逐句比对原文 → 修正🔴/❌ → 客观版（JD模式下额外检查是否虚构了JD技能）
HTML生成:    双页版 + 单页版 + 补充指导（3个HTML；JD模式下补充指导含匹配分析）
PDF导出:    Playwright → A4 print_background=True
```

## 模板文件

- `templates/resume-two-page.html` — 模板 A 双页：深色侧边栏（海军蓝）
- `templates/resume-one-page.html` — 模板 A 单页：深色侧边栏
- `templates/resume-two-page-b.html` — 模板 B 双页：顶部通栏（青绿）
- `templates/resume-one-page-b.html` — 模板 B 单页：顶部通栏
- `templates/resume-two-page-c.html` — 模板 C 双页：经典居中（深蓝金）
- `templates/resume-one-page-c.html` — 模板 C 单页：经典居中
- `templates/resume-two-page-d.html` — 模板 D 双页：现代杂志（黑橙）
- `templates/resume-one-page-d.html` — 模板 D 单页：现代杂志
- `templates/resume-two-page-e.html` — 模板 E 双页：极简线条（靛蓝）
- `templates/resume-one-page-e.html` — 模板 E 单页：极简线条
- `templates/resume-two-page-f.html` — 模板 F 双页：醒目分割（紫色渐变）
- `templates/resume-one-page-f.html` — 模板 F 单页：醒目分割
- `templates/supplement-guide.html` — 补充指导 HTML 骨架（所有模板共用）

## 注意事项

1. **永远先审计再输出**：Phase 3 不可跳过，所有输出必须通过真实性检查
2. **照片保留**：如原文有照片，务必提取并嵌入优化版
3. **中文优先**：所有指导文档和标签使用中文，保持与用户沟通语言一致
4. **不推测技能等级**：原文写"精通"就写"精通"，原文写"熟练"就写"熟练"，不自行升级
5. **证书信息保持原文**：只优化表达，不添加证书编号、有效期等原文没有的信息
6. **JD 可选**：默认不结合 JD 做纯简历优化。用户明确提供 JD 时才启用岗位匹配模式
7. **岗位匹配的底线**：即使在 JD 模式下，也绝不添加候选人不会的设备、没有的证书、虚构的项目。只调整表达侧重点和关键词密度
