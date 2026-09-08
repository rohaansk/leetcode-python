---
number: 15
title: 3Sum
difficulty: Medium
pattern: Sorting + two pointers
date_solved: 2026-09-07
stage_needed: WALKTHROUGH
video: none
review_next: 2026-09-14
---

# 15. 3Sum

[Link to problem](https://leetcode.com/problems/3sum/)

## The problem

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

**Example 1:**
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
The order of the output and the order of the triplets does not matter.

**Example 2:**
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

**Example 3:**
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

**Constraints:**
- 3 <= nums.length <= 3000
- -10^4 <= nums[i] <= 10^4

## Reading the constraints

- `n` up to 3,000 → check the complexity budget table → O(n²) fits, O(n³) doesn't
- Values range from -10⁵ to 10⁵ → numbers can be negative, zero, or positive
- At least 3 elements → always enough to form a triplet

This told me before writing any code: I need an O(n²) solution.

## How I got to the solution

### Step 1 — Reduce the problem

If `a + b + c = 0`, then `b + c = -a`. So if I fix one number, I just need
to find two numbers that add up to its negative. A 3Sum becomes a 2Sum.

### Step 2 — Solve 2Sum first

For 2Sum with a hash map: iterate through the array, for each element check
if `target - element` is already in the map. If yes, found a pair. If no,
add the element to the map. This is O(n).

### Step 3 — Handle duplicates (the hard part)

The problem says no duplicate triplets. With unsorted data and hash maps,
tracking duplicates is messy.

**Sorting solves this.** Sorting puts duplicates next to each other. Now:
- In the outer loop: if `nums[i] == nums[i-1]`, skip — already checked this value
- After finding a match: move both pointers inward, then skip past any duplicates

### Step 4 — Two pointers instead of hash map

Since the array is sorted, 2Sum can use two pointers instead of a hash map:
- `left` starts at `i+1`, `right` starts at the end
- Sum too big → move `right` left
- Sum too small → move `left` right
- Match → record it, move both inward, skip duplicates

This is still O(n) for the inner search but uses O(1) space.

## Complexity

- **Time: O(n²)** — outer loop is O(n), inner two-pointer sweep is O(n).
  The duplicate-skip while loops don't add extra cost because they share the
  same pointers — left can only move right, right can only move left, so the
  total moves per fixed `i` is at most n.
- **Space: O(1)** — ignoring the output list. Sorting is in-place.

## Mistakes I made

1. Wrote `while left > right` instead of `while left < right` — backwards condition
2. Used `nums(i)` instead of `nums[i]` — parentheses call functions, brackets index
3. Forgot `left < right` guard on duplicate-skip while loops — would crash on edge cases

All three were translation errors, not logic errors. The algorithm was right
every time. Lesson: slow down when converting pseudocode to Python.

## What I learned

- **Read constraints first.** They tell you the complexity budget before you
  think about approaches.
- **Sorting is a tool, not just an operation.** It enables two pointers AND
  makes duplicate handling trivial.
- **Reduce the problem.** 3Sum looks hard. 2Sum is easy. Fix one variable
  and a harder problem becomes an easier one.
- **Nested loops don't always multiply.** When inner loops share pointers,
  count total pointer moves, not loop nesting depth.
