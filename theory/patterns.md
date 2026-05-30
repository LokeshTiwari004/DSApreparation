## Two‑Pointer Pattern  
- Idea – Keep two indices that traverse the same array (or string) from opposite ends, from the start, or at different speeds.  
- When to use – Finding pairs/triplets that satisfy a sum/condition, detecting cycles, locating middle element, reversing a list, comparing two sorted sequences.  
- Typical moves  
  1. Both from ends – shrink the window inward (e.g., move left/right based on sum vs. target).  
  2. Same direction – one pointer trails the other (e.g., fast/slow for cycle detection).  
  3. Variable gap – maintain a fixed or dynamic distance (e.g., i and j = i + k).  
- Complexity – O(n) time, O(1) extra space (ignoring output).  
- Key checks – after each move, verify the condition; adjust the pointer that can improve the metric.


## Sliding‑Window Pattern  
- Idea – Treat a contiguous sub‑array (or substring) as a window that expands or contracts while scanning the data structure once.  
- When to use – Problems that ask for the longest/shortest sub‑array meeting a condition, count of sub‑arrays with sum ≤ k, maximum sum of size k, or any “window‑based” aggregate.  
- Typical operations  
  1. Expand – move the right edge (right++) and update the aggregate (sum, frequency map, etc.).  
  2. Shrink – while the window violates the constraint, move the left edge (left++) and adjust the aggregate.  
  3. Record – after each valid expansion, record answer (max length, min length, count, etc.).  
- Complexity – O(n) time because each element enters and leaves the window at most once; O(1)–O(k) space depending on what you store (often a hash map for character frequency).  
- Common variants  
  - Fixed‑size window (e.g., moving average).  
  - Variable‑size window with condition (e.g., “sum ≤ target”).  
  - Two‑pointer window where left and right pointers are the two pointers described above.

Both patterns share the core principle of linear traversal with constant‑space bookkeeping, making them ideal first tools for array‑/string‑focused interview problems. Use the three‑line note after each problem to record: pattern name, edge case you caught, and time/space complexity.