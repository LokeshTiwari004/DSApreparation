# DSA Session — Agent Instructions

## Solution File Convention
- All LeetCode solutions are saved by the LeetCode VSCode extension
- File path: `~/dsa/.leetcode/<ID>.<problem-name-hyphen-separated>.<langext>`
- Examples:
  - `~/dsa/.leetcode/1.two-sum.py`
  - `~/dsa/.leetcode/704.binary-search.py`
  - `~/dsa/.leetcode/53.maximum-subarray.cpp`
- Notes are written as comments inside the solution file (top or bottom)

## When User Reports Solving a Problem
1. Locate the file at `~/dsa/.leetcode/<ID>.<name>.<ext>` — try common extensions: `.py`, `.cpp`, `.c`, `.java`
2. Read the file fully — solution code + comment notes
3. Evaluate:
   - Correctness of approach
   - Pattern label accuracy
   - Time and space complexity correctness
   - Edge case awareness
   - Code style / idiomatic usage for the language
4. Run `date +%d/%m/%y` to get the current date — use this for the log row date
5. Update `~/dsa/log.md` with a new row (see log format below) — Critique column is 1–2 lines only
6. Create a detailed analysis file at `~/dsa/logs/<ID>.<problem-name>.md` (see Per-Problem Log Format below)
7. Deliver critique inline in conversation

## Per-Problem Log Format
File: `~/dsa/logs/<ID>.<problem-name>.md`
Sections to include:
- **Problem** — title, number, difficulty, link
- **User's Approach** — summarise what they did in 2–3 lines
- **Correctness** — does it handle all cases, any bugs found, edge cases missed
- **Pattern Analysis** — correct label or not, what the canonical pattern is, why it applies
- **Complexity** — time and space, correctness of user's stated complexity, optimal complexity if different
- **Code Quality** — style, idioms, readability, language-specific issues
- **Canonical Solution** — clean reference implementation with comments (only if user's solution has meaningful issues or is non-standard)
- **Key Takeaways** — 3–5 bullet points the user should remember from this problem
- **Related Problems** — 2–3 LC problems that use the same pattern

## log.md Format
Each entry is a row in the main table:

| Date | Phase | # | Problem | Pattern | Lang | Time | Hint | Solved | Complexity | Notes (User) | Critique (Agent) |

- **Date**: as reported or from file
- **Phase**: e.g. Phase 1 – Week 1
- **Pattern**: what the user labeled it (correct or not — critique separately)
- **Solved**: Yes / No / Unsolved
- **Notes**: user's own notes summary
- **Critique**: 1–2 line agent remark — flag wrong labels, complexity errors, style issues, or confirm clean

## Language Policy
- Primary language for interviews: **Python**
- Flag any solution written in C or C++ unless user explicitly says they're practising that language
- Do not penalize for language choice, but note the inconsistency

## TODO.md — Problem Queue
- File: `~/dsa/TODO.md`
- Whenever a set of 5 problems is suggested, write them to `TODO.md` as a checklist
- Format each item as: `- [ ] #ID Problem Name — Pattern (Difficulty)`
- When the user reports solving a problem, mark it done: `- [x] #ID Problem Name — Pattern (Difficulty)`
- When ALL 5 items are marked done, reset `TODO.md` with the next set of 5 problems
- Always read `TODO.md` and `completed.txt` before suggesting a new set to avoid duplicates

## solved.md — Progress Reference
- File: `~/dsa/solved.md`
- Updated in two scenarios:
  1. **When TODO.md is revised** (new set of 5 written) — mirror the solved items from the previous set into solved.md
  2. **When an unsolved problem is reported as solved** — move it from Unsolved to Solved section
- Pattern names in solved.md must match the exact convention used in TODO.md entries
- **Difficulty tracking:** when a problem moves from Unsolved → Solved, append `(re-attempt)` to its entry so it's flagged as something that was originally difficult. Also mark any solved problem that took >60 min or required hints with `(hint)`.

## completed.txt — Suggested Problem ID Registry
- File: `~/dsa/completed.txt`
- Contains one problem ID per line — every problem ever suggested, regardless of solve status
- Append new IDs immediately when a set of 5 is written to `TODO.md`
- Before suggesting any problem, check this file — never suggest an ID already listed
- Purpose: single source of truth to prevent duplicate suggestions across sessions

## Roadmap Reference
- Active roadmap: `~/dsa/ROADMAP.md`
- Current phase tracked in `~/dsa/log.md`
