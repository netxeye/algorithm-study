#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
from typing import List

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        tmp = [0]*len(nums)

        def merge(l: int, mid: int, r: int):
            i, j, k = l, mid+1, l
            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    tmp[k] = nums[i]
                    i += 1
                else:
                    tmp[k] = nums[j]
                    j += 1
                k += 1
            while i <= mid:
                tmp[k] = nums[i]
                k += 1
                i += 1
            while j <= r:
                tmp[k] = nums[j]
                k += 1
                j += 1
            for n in range(l,r+1):
                nums[n] = tmp[n]

        def recursion(l: int, r: int):
            if l == r:
                return
            mid = l+(r-l)//2
            recursion(l, mid)
            recursion(mid+1, r)
            merge(l, mid, r)
        
        recursion(0, len(nums)-1)
        return nums
# @lc code=end

