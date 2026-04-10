# Initialization flow

## Goal

Take over project memory management for an existing OpenClaw workspace.

Initialization is responsible for four things:

1. Scan the current project-memory state.
2. Create the minimum shared skeleton when files are missing.
3. Classify existing topics by structure quality.
4. Produce a short takeover report for the user.

Initialization is not responsible for identity setup, persona setup, or creating new project topics from loose mentions in daily memory.

## Scan targets

Check these paths first:

- `memory/`
- `memory/topics/`
- `memory/topics/topics-index.md`
- `memory/YYYY-MM-DD.md` for today

Then inspect existing project topics under `memory/topics/`.

## Topic classification

Classify each discovered topic into one of these states:

### structured

A topic is `structured` when all of these are true:

- `memory/topics/<topic>.md` exists
- `memory/topics/<topic>/00-overview.md` exists
- `memory/topics/<topic>/journal/` exists

This is the preferred long-term form.

### needs-structure

A topic is `needs-structure` when it already exists but is not yet in the preferred form. Common cases:

- only `memory/topics/<topic>.md` exists
- a topic folder exists but has no `00-overview.md`
- a topic folder exists but has no `journal/`
- the entry file and folder both exist, but the folder is incomplete

Do not restructure these topics during initialization. Keep them usable and report them.

### folder-only

A topic is `folder-only` when `memory/topics/<topic>/` exists but `memory/topics/<topic>.md` does not.

Treat this as a migration issue. Report it separately.

## Bootstrap actions

Initialization may do these actions without asking:

- create `memory/`
- create `memory/topics/`
- create today's `memory/YYYY-MM-DD.md`
- create `memory/topics/topics-index.md` when missing

Initialization must not do these actions automatically:

- create a new topic because a project was mentioned in daily memory
- split a single-file topic into a structured folder
- rename topics
- delete old files

## topics-index behavior

If `topics-index.md` is missing, create it from the template and include all discovered topics.

If `topics-index.md` already exists, leave it in place during initialization. Later cleanup can repair or refresh it if the user asks.

## User report

After initialization, send a short takeover report that includes:

- which base files were created,
- how many topics were found,
- structured topics,
- topics that still need structure,
- folder-only anomalies,
- the standing rule that new topics are created only when the user explicitly asks.

## Suggested report shape

```text
项目记忆初始化好了。
我已经补齐了基础骨架，并扫描了现有 topics。
- 新创建：topics-index、今日日记
- 已结构化：InfluenceOS
- 待结构化：job-search、stock-management-system
- 异常：无
后面我会继续按固定规则维护：只有你明确说“新建主题/项目”时，我才创建新的 topic。
```
