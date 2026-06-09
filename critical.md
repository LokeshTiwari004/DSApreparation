# Critical — Problems to Reattempt

## ✅ 875. Koko Eating Bananas — Cleared (08/06/26)

**Pattern:** Binary Search on Answer Space
**Failed:** 2 hours, no hints, wrong approach
**Why saved:** Core pattern that unlocks 20+ problems (Capacity To Ship Packages, Split Array Largest Sum, etc.)

**Quick refresher:**
- Search `k` in range `[1, max(piles)]`
- Feasibility: `sum(ceil(pile/k)) <= h`
- Binary search for minimum feasible `k`

## ✅ 142. Linked List Cycle II — Cleared (08/06/26)

**Pattern:** Floyd's Cycle Detection (Fast & Slow Pointers) + Phase 2
**Crude attempt:** 30 mins, no hints, hashmap O(n) space
**Why saved:** First attempt missed the O(1) space Floyd's solution. Re-attempt used flag-based control flow — should write the clean `while fast and fast.next` + `while slow != fast` pattern from memory.

**Quick refresher:**
- Phase 1: slow 1×, fast 2× → detect cycle, they meet inside cycle
- Phase 2: reset slow to head, both 1× → meet at cycle start
- D = kC − R (math behind why phase 2 works)

---
