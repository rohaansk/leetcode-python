# Problem Log

One block per problem. Fill it in immediately after solving, while it's warm.
The "mistake" line is the highest-value part — read this whole file before an
interview instead of re-reading solutions.

Review schedule: 1 day -> 3 days -> 7 days -> 14 days -> 30 days.
If a cold re-solve fails, reset that problem to 1 day.

---

## Template

```
### [number]. [name]  —  [Easy/Medium/Hard]
Date solved:
Pattern:
Insight (one sentence, no code):
Mistake I made:
Next review:
Video recorded: yes / no
```

---

## 15. 3Sum — Medium

Date solved: 2026-09-07
Pattern: Sorting + two pointers (k-Sum reduction)
Insight: Fix one number and the problem becomes 2Sum; sorting lets you use
two pointers for the inner search AND makes duplicates trivial to skip.
Mistake I made: Wrote `left > right` instead of `left < right`; used `nums(i)`
instead of `nums[i]`; forgot `left < right` guard on duplicate-skip loops.
Next review: 2026-09-14
Video recorded: no

---

## Review queue

| Problem | Pattern | Next review | Last result |
|---------|---------|-------------|-------------|
| 15. 3Sum | Sorting + two pointers | 2026-09-14 | ✅ accepted (beat 70%) |

---

## Patterns covered

Tick these off as you get two clean cold re-solves in each.

- [ ] Two pointers
- [ ] Sliding window
- [ ] Hash map / set lookup
- [ ] Binary search
- [ ] Stack / monotonic stack
- [ ] Linked list (fast & slow pointers)
- [ ] Tree DFS
- [ ] Tree BFS
- [ ] Graph DFS/BFS
- [ ] Backtracking
- [ ] Heap / top-k
- [ ] Intervals
- [ ] Prefix sum
- [ ] Greedy
- [ ] 1D dynamic programming
- [ ] 2D dynamic programming
- [ ] Bit manipulation
- [ ] Trie
- [ ] Union-find
