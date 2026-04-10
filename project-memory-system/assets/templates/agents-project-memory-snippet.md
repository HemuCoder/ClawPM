### 项目记忆默认规则

- 命中项目或长期主题时，先读取 `memory/topics/topics-index.md`。
- 命中已有 topic 后，先读 `memory/topics/<topic>.md`，再读 `memory/topics/<topic>/00-overview.md`。
- 项目协作形成稳定阶段结果后，自动执行一次项目记忆回写。
- `memory/YYYY-MM-DD.md` 只记录简短项目摘要；详细项目过程写入对应 topic 的 `journal/YYYY-MM.md`。
- 只有项目全局状态变化时，才更新 `00-overview.md` 或 `01/02/03...` 文件。
- 只有用户明确说“新建主题 / 新建项目档案”时，才允许创建新的 topic。
