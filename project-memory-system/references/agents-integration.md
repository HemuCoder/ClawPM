# AGENTS.md 集成规则

## 目标

把项目记忆的最小必要规则写进工作区 `AGENTS.md`，让 agent 在日常对话里也会默认执行，而不是只有命中 skill 时才想起这套机制。

## 原则

- 只补最小必要规则，不重写整个 `AGENTS.md`。
- 保留用户已有风格、人格、协作规范。
- 优先把项目记忆规则放进已有“记忆机制 / 主题记忆 / 编码规则之外的工作流规则”附近；如果没有合适位置，再新增一小段。
- 不要写成长篇说明，保持短、硬、可执行。

## 最小常驻规则

应确保 `AGENTS.md` 至少表达出这些意思：

1. 命中项目或长期主题时，先读取 `memory/topics/topics-index.md`。
2. 命中已有 topic 后，先读 `memory/topics/<topic>.md`，再读 `memory/topics/<topic>/00-overview.md`。
3. 项目协作形成稳定阶段结果后，自动执行一次项目记忆回写。
4. `memory/YYYY-MM-DD.md` 只写简短项目摘要。
5. 详细项目过程写进 `memory/topics/<topic>/journal/YYYY-MM.md`。
6. 只有项目全局状态变化时，才更新 `00-overview.md` 或 `01/02/03...`。
7. 只有用户明确说“新建主题 / 新建项目档案”时，才允许创建新的 topic。
8. 如果项目在本轮对话中已推进，但随后切换到别的话题并进入收尾，也要检查是否需要做一次项目记忆回写。
9. 初始化完成后的首次引导里，要提醒用户：手动 `/new` 开新会话前，先让 agent 更新本轮项目记忆。

## 建议插入片段

可将下面这段合并进 `AGENTS.md` 的记忆机制部分：

```md
### 项目记忆默认规则

- 命中项目或长期主题时，先读取 `memory/topics/topics-index.md`。
- 命中已有 topic 后，先读 `memory/topics/<topic>.md`，再读 `memory/topics/<topic>/00-overview.md`。
- 项目协作形成稳定阶段结果后，自动执行一次项目记忆回写。
- `memory/YYYY-MM-DD.md` 只记录简短项目摘要；详细项目过程写入对应 topic 的 `journal/YYYY-MM.md`。
- 只有项目全局状态变化时，才更新 `00-overview.md` 或 `01/02/03...` 文件。
- 只有用户明确说“新建主题 / 新建项目档案”时，才允许创建新的 topic。
```

## 初始化后的要求

初始化完成后，应确认：

- `AGENTS.md` 已包含上述最小规则或等价表达；
- 后续普通项目对话，即使没有再次显式提到这个 skill，agent 也能按这些规则工作。
