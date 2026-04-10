# 初始化流程

## 目标

接管一个现有 OpenClaw 工作区中的**项目记忆系统**。

初始化只负责四件事：

1. 扫描当前项目记忆状态。
2. 在缺失时补齐最低公共骨架。
3. 对现有 topic 的结构完整度做分类。
4. 生成一份简短的接管结果，供 agent 向用户汇报。

初始化**不负责**：

- 身份设定
- 人格设定
- 用户画像初始化
- 因为 daily memory 里提到某个项目就自动新建 topic

## 扫描范围

优先检查这些路径：

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

## 初始化禁止自动执行的动作

以下动作初始化阶段不能擅自执行：

- 因为在 daily memory 里看到某个项目，就自动创建新 topic
- 把单文件 topic 自动拆成结构化目录
- 重命名 topic
- 删除旧文件

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
- 后续会继续遵守“只有用户明确要求时才创建新 topic”的规则

## 建议汇报格式

```text
项目记忆初始化好了。
我已经补齐了基础骨架，并扫描了现有 topics。
- 新创建：topics-index、今日日记
- 已结构化：InfluenceOS
- 待结构化：job-search、stock-management-system
- 异常：无
后面我会继续按固定规则维护：只有你明确说“新建主题/项目”时，我才创建新的 topic。
```
