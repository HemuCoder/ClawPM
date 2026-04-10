---
name: project-memory-system
description: Manage OpenClaw project memory with a local topics-based file system. Use when initializing or repairing `memory/topics`, bootstrapping `topics-index.md` and today's daily memory, scanning existing project memories, classifying topics as structured vs needing structure, or maintaining project memory without creating new topics unless the user explicitly asks to create one.
---

# Project Memory System

Manage project memory only. Do not use this skill for persona, identity, or user-profile initialization.

## Core rules

- Create a new topic only when the user explicitly asks to create a new topic or project archive.
- Initialize only the project-memory skeleton; do not auto-create topic files for projects discovered only in daily memory.
- Keep `memory/topics/<topic>.md` lightweight. Treat it as an entry file, not the full archive.
- Treat `00-overview.md` as the only required file inside a structured topic folder. Other `01/02/03...` files are optional and project-specific.
- Do not restructure old topics during initialization unless the user explicitly asks for restructuring.

## Initialization workflow

When the user asks to set up or repair project memory:

1. Read `references/initialization-flow.md`.
2. Run `scripts/init_project_memory.py --workspace <target-workspace>`.
3. Review the report from the script.
4. Tell the user:
   - what skeleton files were created,
   - how many topics were found,
   - which topics are already structured,
   - which topics still need structure,
   - that new topics will only be created on explicit request.
5. If the report shows older topics that need structure, keep using them as-is for now and mention them as candidates for later cleanup.

## Working with existing topics

When a request hits an existing topic:

1. Read the topic entry file first: `memory/topics/<topic>.md`.
2. If the topic has a folder, read `00-overview.md` next.
3. Read `01/02/03...` files only when the current task needs them.
4. Read the current journal file only when recent execution history matters.

## Initialization deliverable

Initialization should leave the workspace in this minimum state:

```text
memory/
├── YYYY-MM-DD.md
└── topics/
    └── topics-index.md
```

If topics already exist, initialization should classify them and report their status. It should not auto-create or auto-restructure project archives.
