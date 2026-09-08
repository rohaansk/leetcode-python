"""
15. 3Sum — Medium
https://leetcode.com/problems/3sum/

Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.

Pattern: Sorting + Two Pointers
Time:    O(n^2)  — outer loop O(n) × inner two-pointer sweep O(n)
Space:   O(1)    — ignoring the output list; sorting is in-place

Key insight: Fix one number and the problem becomes 2Sum.
Sorting makes the inner search O(n) with two pointers AND puts
duplicates next to each other so they're trivial to skip.
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []

        for i in range(len(nums) - 1):
            # Skip duplicate values for the fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                pass
            else:
                left = i + 1
                right = len(nums) - 1

                while left < right:
                    total = nums[left] + nums[right]

                    if total > -nums[i]:
                        # Sum too big — shrink from the right
                        right -= 1
                    elif total < -nums[i]:
                        # Sum too small — grow from the left
                        left += 1
                    else:
                        # Found a valid triplet
                        results.append([nums[i], nums[left], nums[right]])

                        # Move both pointers inward
                        left += 1
                        right -= 1

                        # Skip duplicates on the left
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Skip duplicates on the right
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return results
