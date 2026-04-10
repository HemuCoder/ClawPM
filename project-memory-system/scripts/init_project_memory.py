#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path

STATUS_LABELS = {
    "structured": "已结构化",
    "needs-structure": "待结构化",
    "folder-only": "仅目录无入口",
}

TOPICS_INDEX_TEMPLATE = """# 主题索引

这个文件是主题记忆的总入口。

## 使用规则

- 每次会话启动时先读取本文件，了解当前有哪些可复用主题。
- 当用户提到明确项目/主题时，先看这里是否已有命中项。
- 命中后再读取对应 topic 文件。
- 新建主题后，要立刻在这里补一条索引。
- 主题结束或失效后，不要删历史；更新状态即可。

## 加载 checklist

1. 读取本文件
2. 识别用户当前提到的项目/主题/关键词
3. 命中后读取对应 topic 文件
4. 结合今天/昨天的日记继续工作
5. 结束后回写 topic 文件与当日日记

## 主题目录

| 主题 | 关键词/触发词 | 文件 | 当前状态 | 最近更新 |
|---|---|---|---|---|
{rows}
"""

DAILY_TEMPLATE = """# {today}

- 初始化或当天发生的重要事项写在这里。
- 记录今天的推进、判断、用户新规则、后续要回看的线索。
- 这是原始经过，不是长期提炼。
"""


@dataclass
class TopicState:
    name: str
    entry: bool
    folder: bool
    overview: bool
    journal: bool
    status: str
    status_label: str
    path: str


@dataclass
class Report:
    workspace: str
    created: list[str]
    topics_found: int
    structured: list[str]
    needs_structure: list[str]
    folder_only: list[str]
    topic_states: list[TopicState]
    summary: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="初始化 OpenClaw 项目记忆骨架")
    parser.add_argument("--workspace", default=".", help="目标工作区路径")
    parser.add_argument("--today", default=date.today().isoformat(), help="今天的日期，用于生成今日日记文件")
    return parser.parse_args()


def ensure_dir(path: Path, created: list[str]) -> None:
    if path.exists():
        return
    path.mkdir(parents=True, exist_ok=True)
    created.append(str(path))


def write_if_missing(path: Path, content: str, created: list[str]) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    created.append(str(path))


def discover_topics(topics_dir: Path) -> list[TopicState]:
    entry_names = {p.stem for p in topics_dir.glob("*.md") if p.name != "topics-index.md"}
    folder_names = {p.name for p in topics_dir.iterdir() if p.is_dir() and not p.name.startswith(".")}
    names = sorted(entry_names | folder_names)
    states: list[TopicState] = []
    for name in names:
        entry_path = topics_dir / f"{name}.md"
        folder_path = topics_dir / name
        overview_path = folder_path / "00-overview.md"
        journal_path = folder_path / "journal"
        entry = entry_path.is_file()
        folder = folder_path.is_dir()
        overview = overview_path.is_file()
        journal = journal_path.is_dir()
        if entry and overview and journal:
            status = "structured"
        elif folder and not entry:
            status = "folder-only"
        else:
            status = "needs-structure"
        path = f"memory/topics/{name}.md" if entry else f"memory/topics/{name}/"
        states.append(TopicState(name, entry, folder, overview, journal, status, STATUS_LABELS[status], path))
    return states


def render_rows(states: list[TopicState], today: str) -> str:
    if not states:
        return "| 示例主题 | 示例关键词 | `memory/topics/example-topic.md` | 待创建/运行中/已归档 | YYYY-MM-DD |"
    rows = []
    for state in states:
        rows.append(f"| {state.name} |  | `{state.path}` | {state.status_label} | {today} |")
    return "\n".join(rows)


def render_summary(created: list[str], structured: list[str], needs_structure: list[str], folder_only: list[str]) -> str:
    created_labels = "、".join(Path(path).name for path in created) if created else "无"
    structured_labels = "、".join(structured) if structured else "无"
    pending_labels = "、".join(needs_structure) if needs_structure else "无"
    anomaly_labels = "、".join(folder_only) if folder_only else "无"
    return (
        "项目记忆初始化好了。\n"
        "我已经补齐了基础骨架，并扫描了现有 topics。\n"
        f"- 新创建：{created_labels}\n"
        f"- 已结构化：{structured_labels}\n"
        f"- 待结构化：{pending_labels}\n"
        f"- 异常：{anomaly_labels}\n"
        "后面我会继续按固定规则维护：只有你明确说“新建主题/项目”时，我才创建新的 topic。"
    )


def main() -> None:
    args = parse_args()
    workspace = Path(args.workspace).expanduser().resolve()
    memory_dir = workspace / "memory"
    topics_dir = memory_dir / "topics"
    topics_index = topics_dir / "topics-index.md"
    daily_file = memory_dir / f"{args.today}.md"

    created: list[str] = []
    ensure_dir(memory_dir, created)
    ensure_dir(topics_dir, created)

    states = discover_topics(topics_dir)
    write_if_missing(topics_index, TOPICS_INDEX_TEMPLATE.format(rows=render_rows(states, args.today)), created)
    write_if_missing(daily_file, DAILY_TEMPLATE.format(today=args.today), created)

    states = discover_topics(topics_dir)
    structured = [state.name for state in states if state.status == "structured"]
    needs_structure = [state.name for state in states if state.status == "needs-structure"]
    folder_only = [state.name for state in states if state.status == "folder-only"]
    report = Report(
        workspace=str(workspace),
        created=created,
        topics_found=len(states),
        structured=structured,
        needs_structure=needs_structure,
        folder_only=folder_only,
        topic_states=states,
        summary=render_summary(created, structured, needs_structure, folder_only),
    )
    payload = asdict(report)
    payload["topic_states"] = [asdict(state) for state in report.topic_states]
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
