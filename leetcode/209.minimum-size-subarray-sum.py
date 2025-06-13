#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
from typing import List
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, n, shortest= 0, len(nums), float('inf')
        sub_total = 0
        if n < 2:
            if n == 0 :
                return n
            return n if nums[0] >= target else 0
        for r in range(n):
            sub_total += nums[r]
            while l <= r and sub_total >= target:
                shortest = min(shortest, r-l+1)
                sub_total -= nums[l]
                l += 1
        return shortest if shortest != float('inf') else 0

# @lc code=end

