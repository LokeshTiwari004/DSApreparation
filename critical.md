# Critical — Problems to Reattempt

## 875. Koko Eating Bananas

**Pattern:** Binary Search on Answer Space
**Failed:** 2 hours, no hints, wrong approach
**Why saved:** Core pattern that unlocks 20+ problems (Capacity To Ship Packages, Split Array Largest Sum, etc.)

**Quick refresher:**
- Search `k` in range `[1, max(piles)]`
- Feasibility: `sum(ceil(pile/k)) <= h`
- Binary search for minimum feasible `k`

**Solve again when:** After completing Week 3 (Stacks & Queues)

---

## 142. Linked List Cycle II

**Pattern:** Floyd's Cycle Detection (Fast & Slow Pointers) + Phase 2
**Crude attempt:** 30 mins, no hints, hashmap O(n) space
**Why saved:** First attempt missed the O(1) space Floyd's solution. Re-attempt used flag-based control flow — should write the clean `while fast and fast.next` + `while slow != fast` pattern from memory.

**Quick refresher:**
- Phase 1: slow 1×, fast 2× → detect cycle, they meet inside cycle
- Phase 2: reset slow to head, both 1× → meet at cycle start
- D = kC − R (math behind why phase 2 works)

**Solve again when:** Before Phase 3 (mock assessments)

---

## 19. Remove Nth Node From End of List

**Pattern:** Two Pointers (fixed gap)
**Crude attempt:** Lag counter with head-removal special case
**Why saved:** Non-standard lag counter approach. Should internalize the dummy node + gap pattern.

**Quick refresher:**
- `dummy = ListNode(0, head); slow = fast = dummy`
- Advance `fast` by `n` first
- Move both until `fast.next` is None
- `slow.next = slow.next.next`
- Return `dummy.next`

**Solve again when:** Before Phase 3 (mock assessments)
