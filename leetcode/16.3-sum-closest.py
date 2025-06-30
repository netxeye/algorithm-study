#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

from typing import List


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n  = len(nums)
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return total  
                closest = total if abs(target - total) < abs(target - closest) else closest
        return closest

# @lc code=end