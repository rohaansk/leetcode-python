"""
LeetCode 0. Problem Name  —  Medium
Pattern: ...
Time: O(?)   Space: O(?)

Insight: one sentence, no code.
"""


class Solution:
    def methodName(self, nums: list[int]) -> list[int]:
        # 1. plain-English step
        # 2. plain-English step
        # 3. plain-English step
        pass


if __name__ == "__main__":
    # Cases I want to check by hand, including the ones that broke me.
    cases = [
        ([1, 2, 3], "expected"),
    ]
    for args, expected in cases:
        got = Solution().methodName(args)
        status = "ok " if got == expected else "FAIL"
        print(f"{status} {args} -> {got}  (expected {expected})")
