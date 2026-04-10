---
name: project-memory-system
description: 用本地 `memory/topics` 文件体系管理 OpenClaw 的项目记忆。适用于：初始化或修复 `memory/topics`、补齐 `topics-index.md` 与今日日记、扫描现有项目记忆并修正 AGENTS.md 中的常驻项目记忆规则；当用户恢复某个已有项目、继续推进长期主题、询问某项目下一步、或一次项目协作完成子任务/形成稳定结论/更新关键卡点/明确下一步时，按“daily 简写、journal 详写、overview 按需更新”的规则读取并回写项目记忆。只有当用户明确要求“新建主题/项目”时，才允许创建新的 topic。
---

# 项目记忆系统

这个 skill 只负责**项目记忆 / topic 记忆**，不负责人格、身份或用户画像初始化。

## 核心规则

- 只有用户明确要求“新建主题 / 新建项目档案”时，才允许创建新的 topic。
- 初始化时只补齐项目记忆骨架，不因为 daily memory 里提到某个项目就自动建 topic。
- 初始化完成后，要把最小必要的项目记忆规则写入工作区 `AGENTS.md`，让这套机制成为常驻行为，而不只是一次性 skill。
- `memory/topics/<topic>.md` 必须保持轻量，只做入口文件，不承载整份项目档案。
- 结构化 topic 目录里，`00-overview.md` 是唯一必需文件；`01/02/03...` 文件按项目类型自由扩展。
- 初始化时不要擅自重构旧 topic；只识别、分类、汇报，等用户明确要求后再整理。
- `memory/YYYY-MM-DD.md` 只记录**简短项目摘要**，避免前一日日记自动加载时占用过多上下文。
- `memory/topics/<topic>/journal/YYYY-MM.md` 记录**详细项目推进过程**，供后续按项目命中后渐进加载。
- `00-overview.md` 与 `01/02/03...` 只维护长期有效的项目状态与结构化认知，不写流水账。

## 初始化流程

当用户要求初始化、修复、接管项目记忆时：

1. 读取 `references/initialization-flow.md`。
2. 运行 `scripts/init_project_memory.py --workspace <目标工作区>`。
3. 按 `references/agents-integration.md` 中的规则检查并更新工作区 `AGENTS.md`，把最小常驻项目记忆规则写进去。
4. 查看脚本输出的初始化结果与中文摘要。
5. 向用户汇报：
   - 新补齐了哪些基础文件；
   - 扫描到了多少个 topic；
   - 哪些 topic 已结构化；
   - 哪些 topic 还待结构化；
   - 是否存在只有目录没有入口文件的异常；
   - `AGENTS.md` 是否已补齐项目记忆常驻规则；
   - 后续将继续遵守“只有用户明确要求时才新建 topic”的规则。
6. 如果发现旧 topic 结构不完整，先继续沿用，不要在初始化阶段直接改结构；把它们作为后续可整理对象说明给用户。

## 日常维护流程

当用户正在推进一个已有项目，或当前协作形成了一个**稳定阶段结果**时：

1. 读取 `references/writeback-rules.md`。
2. 命中已有 topic 时，先读 `memory/topics/<topic>.md`，再读 `00-overview.md`。
3. 只在当前任务确实需要时，按需读取 `01/02/03...` 文件与当月 `journal`。
4. 当出现以下任一情况时，执行一次项目记忆回写：
   - 完成了一个明确子任务；
   - 形成了稳定结论；
   - 发现或解决了关键卡点；
   - 明确了下一步。
5. 回写时遵守三层规则：
   - `memory/YYYY-MM-DD.md`：写简短摘要；
   - `journal/YYYY-MM.md`：写详细过程；
   - `00-overview.md` / `01/02/03...`：仅在项目全局状态改变时更新。
6. 如果旧 topic 结构不理想，先继续当前任务，再轻量提醒后续可整理；不要因为结构问题中断当前协作。

## 使用已有 topic

当任务命中已有 topic 时：

1. 先读入口文件：`memory/topics/<topic>.md`。
2. 如果该 topic 有目录，再读 `00-overview.md`。
3. 只在当前任务确实需要时，按需读取 `01/02/03...` 文件。
4. 只有在最近推进历史会影响当前判断时，才读取当月 `journal`。

## 初始化完成的最低交付

初始化后，工作区至少应具备：

```text
memory/
├── YYYY-MM-DD.md
└── topics/
    └── topics-index.md
```

并且工作区 `AGENTS.md` 中应具备最小必要的项目记忆常驻规则。

如果工作区里已经存在旧 topic，初始化应完成分类并汇报状态；但不应自动创建新项目档案，也不应自动拆分旧 topic 结构。
