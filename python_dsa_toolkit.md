# Python DSA Toolkit
My personal reference for LeetCode. Add to this every time I look something up —
in my own words, with the problem that made me need it.
---
## Sorting
```python
nums.sort()                          # in place, returns None
s = sorted(nums)                     # returns a new list
sorted(nums, reverse=True)           # descending
sorted(pairs, key=lambda x: x[1])    # by second element of each tuple
sorted(words, key=len)               # by length
sorted(items, key=lambda x: (-x[1], x[0]))   # by count desc, then name asc
```
## Looping
```python
for i, val in enumerate(nums):       # index and value together
for a, b in zip(list1, list2):       # two lists in parallel
for i in range(len(nums) - 1, -1, -1):   # backwards
for ch in "hello":                   # strings are iterable
```
## Slicing
```python
nums[::-1]     # reversed copy
nums[2:5]      # elements 2,3,4
nums[:3]       # first three
nums[-1]       # last element
nums[-2:]      # last two
```
## Sets — O(1) membership
```python
seen = set()
seen.add(x)
if x in seen: ...
seen.remove(x)
set(nums)                  # dedupe a list
set(a) & set(b)            # intersection
set(a) | set(b)            # union
```
## Dicts
```python
count = {}
count[x] = count.get(x, 0) + 1      # count without KeyError
for key in d: ...
for key, val in d.items(): ...
d.keys(), d.values()
if key in d: ...
```
## collections — the big unlock
```python
from collections import defaultdict, Counter, deque
d = defaultdict(list)      # missing key auto-creates an empty list
d[key].append(val)         # no "if key not in d" needed
d = defaultdict(int)       # missing key auto-creates 0
d[key] += 1
c = Counter(nums)          # {value: how many times}
c.most_common(2)           # top 2 as list of (value, count)
c[x]                       # returns 0 for missing, no KeyError
q = deque()                # queue: O(1) at BOTH ends
q.append(x)                # add right
q.popleft()                # remove left  <- BFS workhorse
q.appendleft(x); q.pop()   # the other two
```
## Numbers
```python
float('inf'), float('-inf')     # for "best so far" initialization
best = min(best, candidate)
best = max(best, candidate)
abs(x)
a // b        # integer division (floors toward -inf, careful with negatives)
a % b
divmod(a, b)  # (quotient, remainder)
```
## Heaps — top-k, "smallest so far"
```python
import heapq
h = []
heapq.heappush(h, val)
heapq.heappop(h)            # always pops the SMALLEST
h[0]                        # peek smallest without removing
heapq.heapify(nums)         # turn a list into a heap in place, O(n)
heapq.nlargest(k, nums)
heapq.nsmallest(k, nums)
# max-heap trick: push negatives, negate on the way out
heapq.heappush(h, -val)
biggest = -heapq.heappop(h)
# heap of pairs sorts by first element
heapq.heappush(h, (count, word))
```
## Strings
```python
"".join(chars)        # list of chars -> string
",".join(words)
s.split()             # split on whitespace
s.split(",")
s.strip()
s.lower(), s.upper()
s.isalnum(), s.isdigit(), s.isalpha()
ord('a')   # 97   char -> number
chr(97)    # 'a'  number -> char
s.replace(old, new)
s.startswith(p), s.endswith(p)
```
Strings are immutable — to build one up, collect into a list and `"".join()` at the end.
## Building output
```python
res = []
res.append([a, b, c])
res.extend(other_list)
[x * 2 for x in nums]                  # list comprehension
[x for x in nums if x > 0]             # with a filter
[[0] * cols for _ in range(rows)]      # 2D grid — DON'T use [[0]*cols]*rows
```
That last one is a real trap: `[[0]*3]*2` makes two references to the SAME row.
## Two-pointer template
```python
left, right = 0, len(nums) - 1
while left < right:
    # compute something from nums[left] and nums[right]
    if too_small:
        left += 1
    elif too_big:
        right -= 1
    else:
        # record, then move both
        left += 1
        right -= 1
```
## Sliding window template
```python
left = 0
for right in range(len(nums)):
    # expand: add nums[right] to the window
    while window_is_invalid:
        # shrink: remove nums[left]
        left += 1
    # window is valid here — record the answer
```
## BFS template
```python
from collections import deque
q = deque([start])
seen = {start}
while q:
    node = q.popleft()
    for nxt in neighbours(node):
        if nxt not in seen:
            seen.add(nxt)
            q.append(nxt)
```
## DFS template (recursive)
```python
def dfs(node, seen):
    if node in seen:
        return
    seen.add(node)
    for nxt in neighbours(node):
        dfs(nxt, seen)
```
## Reading constraints — do this FIRST
Every LeetCode problem has a "Constraints" section at the bottom. Read it
before you think about code. It tells you two things:
**1. What your inputs look like**
- How big can the array/string be? (upper bound on n)
- Can values be negative? Zero? Very large?
- Are there at least k elements? (lower bound — edge cases you DON'T need to handle)
**2. What speed your solution needs**
A computer does roughly **10^8 (100 million) simple operations per second**.
LeetCode gives you a few seconds, so ~10^8 is your safe budget.
Plug n into your Big-O formula and compare:
- n = 3,000 → O(n²) = 9,000,000 → well under 10^8 ✓
- n = 3,000 → O(n³) = 27,000,000,000 → way over 10^8 ✗
**The routine every time:**
1. Read constraints
2. Find n (the biggest input size)
3. Look up n in the table below → that's the slowest acceptable Big-O
4. NOW start thinking about approaches
Learned this on: 3Sum (#15). n ≤ 3,000, so O(n²) passes but O(n³) doesn't.
## Complexity budget
n is the input size from the constraints. Roughly 10^8 simple operations per second.
| n up to      | what fits          |
|--------------|--------------------|
| 10           | O(n!) / O(2^n)     |
| 20-25        | O(2^n)             |
| 500          | O(n^3)             |
| 5,000        | O(n^2)             |
| 100,000      | O(n log n)         |
| 1,000,000+   | O(n)               |
Read the constraints BEFORE coding — they tell you which complexity to aim for.
---
## Things I looked up
<!-- Add here, in my own words, with the problem that needed it -->
