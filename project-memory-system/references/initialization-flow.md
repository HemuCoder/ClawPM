# 初始化流程

## 目标

接管一个现有 OpenClaw 工作区中的**项目记忆系统**，并把最小必要规则落进 `AGENTS.md`，让项目记忆机制在后续日常对话中持续生效。

初始化只负责五件事：

1. 扫描当前项目记忆状态。
2. 在缺失时补齐最低公共骨架。
3. 对现有 topic 的结构完整度做分类。
4. 检查并更新工作区 `AGENTS.md` 的最小项目记忆规则。
5. 生成一份简短的接管结果与一次性使用引导，供 agent 向用户汇报。

初始化**不负责**：

- 身份设定
- 人格设定
- 用户画像初始化
- 因为 daily memory 里提到某个项目就自动新建 topic

## 扫描范围

优先检查这些路径：

- `AGENTS.md`
- `memory/`
- `memory/topics/`
- `memory/topics/topics-index.md`
- 今天的 `memory/YYYY-MM-DD.md`

然后检查 `memory/topics/` 下现有的项目 topic。

## topic 分类规则

每个发现的 topic 都要分到以下状态之一：

### 已结构化

满足以下条件时，判定为“已结构化”：

- `memory/topics/<topic>.md` 存在
- `memory/topics/<topic>/00-overview.md` 存在
- `memory/topics/<topic>/journal/` 存在

这是长期维护时的推荐形态。

### 待结构化

当 topic 已存在，但还没达到推荐结构时，判定为“待结构化”。常见情况：

- 只有 `memory/topics/<topic>.md`
- 目录已存在，但缺 `00-overview.md`
- 目录已存在，但缺 `journal/`
- 入口文件和目录都存在，但目录仍不完整

初始化阶段不要重构这些 topic，只需继续保持可用并在汇报中指出。

### 仅目录无入口

当 `memory/topics/<topic>/` 存在，但 `memory/topics/<topic>.md` 不存在时，判定为“仅目录无入口”。

这通常说明历史迁移不完整，需要单独记录为异常项。

## 初始化可自动执行的动作

以下动作可以直接执行，无需额外确认：

- 创建 `memory/`
- 创建 `memory/topics/`
- 创建今天的 `memory/YYYY-MM-DD.md`
- 在缺失时创建 `memory/topics/topics-index.md`
- 按最小规则补齐或更新 `AGENTS.md` 中的项目记忆常驻部分

## 初始化禁止自动执行的动作

以下动作初始化阶段不能擅自执行：

- 因为在 daily memory 里看到某个项目，就自动创建新 topic
- 把单文件 topic 自动拆成结构化目录
- 重命名 topic
- 删除旧文件
- 重写整个 `AGENTS.md`，覆盖用户已有规则

## AGENTS.md 规则

初始化时应参考 `references/agents-integration.md`，把最小必要的项目记忆规则写入工作区 `AGENTS.md`。

目标不是重写整个 `AGENTS.md`，而是确保后续日常对话里，agent 默认知道：

- 命中项目时先查 `topics-index.md`
- 命中 topic 后先读入口文件和 `00-overview.md`
- 项目形成稳定阶段结果后自动执行一次回写
- `daily` 简写、`journal` 详写
- 新 topic 只有用户明确要求时才创建

## topics-index 规则

如果 `topics-index.md` 缺失，则用模板创建，并把当前已发现的 topic 写入索引。

如果 `topics-index.md` 已存在，初始化阶段默认保留原文件，不直接重写；后续如用户明确要求清理或刷新，再处理。

## 初始化完成后的用户汇报

汇报中至少要包含：

- 新创建了哪些基础文件
- 总共发现多少个 topic
- 哪些 topic 已结构化
- 哪些 topic 待结构化
- 哪些 topic 存在“仅目录无入口”异常
- `AGENTS.md` 是否已补齐项目记忆常驻规则
- 后续会继续遵守“只有用户明确要求时才创建新 topic”的规则
- 一次性提醒用户：如果准备手动 `/new` 开新会话，先让 agent 更新本轮项目记忆，避免当前会话里尚未回写的项目推进丢失
