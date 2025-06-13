#
# @lc app=leetcode id=35 lang=python3
# @lcpr version=30201
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > target:
                l = mid+1
            elif nums[mid] < target:
                r = mid-1
            else:
                return mid
        return mid+1
        
# @lc code=end



#
# @lcpr case=start
# [1,3,5,6]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n7\n
# @lcpr case=end

#

