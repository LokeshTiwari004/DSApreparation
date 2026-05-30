# DSA Roadmap — Interview Prep

**Profile:** Data Science student | Python | ~65 min/day | 2‑month sprint + long‑term GATE prep  
**Approach:** Problem‑based | 20‑min rule | LeetCode primary  
**Immediate Goal:** Clear Easy–Medium assessments at lower/mid‑tier companies within 2 months  
**Long‑term Goal:** GATE + top‑tier SDE/DS roles  

---

## Ground Rules

1. **20‑min rule** — struggle independently for 20 minutes, then study the solution deeply. Never skip understanding *why*.
2. **3‑line note after every problem** — pattern used, edge case caught, time complexity. This becomes your personal pattern book.
3. **Re‑solve problems after 1 week** — cold recall is the real test, not first‑time solve.
4. **Track a daily log** — date, problem number, time taken, solved/unsolved.
5. **Use agentic tools (OpenCode)** for theory gaps, solution breakdowns, custom problems, and test‑case generation.

---

## Daily Session Structure (65 min)

| Time | Activity |
|------|----------|
| 0–10 min | Re‑read yesterday's solution cold — no looking at code |
| 10–55 min | Solve 2 new problems (20‑min rule each) |
| 55–65 min | Write 3‑line note: pattern, edge case, complexity |

---

## Phase 1 – Foundation Sprint (Weeks 1‑3)

> **Goal:** Rebuild theory as code. Every concept = at least 3 problems solved.

| Week | Topics | Difficulty | Problems / Day |
|------|--------|------------|----------------|
| 1 | Arrays, Strings, Two Pointers, Sliding Window | Easy → Medium | 2 |
| 2 | Hashing, Prefix Sum, Binary Search | Easy → Medium | 2 |
| 3 | Stacks, Queues, Monotonic Stack | Easy → Medium | 2 |

### Week 1 Starter Problems

| # | Problem | LC Number | Pattern |
|---|---------|-----------|---------|
| 1 | Two Sum | #1 | Hashing |
| 2 | Best Time to Buy and Sell Stock | #121 | Sliding Window |
| 3 | Contains Duplicate | #217 | Hashing |
| 4 | Maximum Subarray | #53 | Kadane's Algorithm |
| 5 | Longest Substring Without Repeating Characters | #3 | Sliding Window |

---

## Phase 2 – Core Patterns (Weeks 4‑6)

> **Goal:** Pattern recognition over brute‑force thinking.

| Week | Topics | Difficulty | Problems / Day |
|------|--------|------------|----------------|
| 4 | Linked Lists (all variants), Fast & Slow Pointers | Easy → Medium | 2 |
| 5 | Recursion, Backtracking, Trees (DFS/BFS) | Medium | 1–2 |
| 6 | Graphs (BFS/DFS/Cycle Detection), Sorting Internals | Medium | 1–2 |

---

## Phase 3 – Assessment Readiness (Weeks 7‑8)

> **Goal:** Simulate real assessments. Speed + accuracy under pressure.

| Week | Activity |
|------|----------|
| 7 | Mixed‑topic revision — 1 problem per major topic daily. Hard 30‑min cap per problem. |
| 8 | Full mock assessments — 2–3 problems in 60–90 min sessions. Review all weak spots. |

**Milestone:** By the end of Week 8, you should solve ≥ 80 % of attempted Easy‑Medium problems within the time limit and achieve a post‑review time ≤ 5 min per problem.

---

## Phase 4 – Long‑Term Continuation (Month 3+)

> **Goal:** Prepare for GATE and top‑tier company interviews.

- [ ] Dynamic Programming (critical for GATE + top companies)
- [ ] Heaps & Priority Queues
- [ ] Tries
- [ ] Segment Trees & Fenwick Trees
- [ ] Advanced Graphs — Dijkstra, Topological Sort, Union‑Find
- [ ] Bit Manipulation
- [ ] System Design basics (for SDE interviews)
- [ ] LeetCode Weekly Contests — benchmark progress regularly

*(Add an estimated week range next to each item when you schedule them.)*

---

## Topic → Pattern Reference

| Topic | Key Patterns to Learn |
|-------|-----------------------|
| Arrays | Two Pointers, Sliding Window, Prefix Sum, Kadane's |
| Strings | Sliding Window, Hashing, Two Pointers |
| Hashing | Frequency maps, Anagram detection, Subarray sum |
| Binary Search | Search on answer, Rotated arrays, Lower/Upper bound |
| Stacks | Monotonic stack, Next greater element, Valid parentheses |
| Linked Lists | Fast & Slow pointers, Reversal, Merge |
| Trees | DFS (preorder/inorder/postorder), BFS (level order), LCA |
| Graphs | BFS shortest path, DFS cycle detection, Connected components |
| Recursion | Tree of choices, Base case design, Memoization intro |
| Backtracking | Subsets, Permutations, N‑Queens style |
| DP (Phase 4) | 1D DP, 2D DP, Knapsack, LCS, LIS |

*See `references/patterns.md` for detailed explanations and templates.*

---

## Progress Log

> Add a row daily.

| Date | Problem | LC # | Difficulty | Time Taken | Solved? | Pattern |
|------|---------|------|------------|------------|---------|---------|
|      |         |      |            |            |         |         |

<!-- Fill in daily entries -->

---

## Additional Best Practices

### Do
- ✅ Start with brute force, then optimize
- ✅ Write test cases first
- ✅ Analyze time/space complexity
- ✅ Practice the same pattern repeatedly
- ✅ Explain your approach out loud
- ✅ Use real‑product context to remember
- ✅ Code in your target interview language

### Don't
- ❌ Jump to the optimal solution immediately
- ❌ Skip complexity analysis
- ❌ Memorize solutions without understanding
- ❌ Practice only easy problems
- ❌ Ignore edge cases
- ❌ Code in silence (practice explaining)
- ❌ Give up after one attempt

### Spaced‑Repetition Reminder
- Review each solved problem after **1 week**, then after **1 month**, and finally after **3 months** to cement retention.

---

## Resources

- **Primary practice:** [LeetCode](https://leetcode.com) — filter by topic + difficulty
- **Theory + GATE:** GeeksforGeeks — use alongside Phase 4
- **Local tools:** OpenCode — theory on demand, custom problems, test case generation, solution debugging
