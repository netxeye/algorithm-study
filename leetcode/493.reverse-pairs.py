#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#
from typing import List

# @lc code=start


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        length_ = len(nums)
        tmp = [0] * length_

        def merge(l: int, mid: int, r: int) -> int:
            total = sub_total = 0
            right = mid+1
            for left in range(l, mid+1):
                while right <= r and nums[right]*2 < nums[left]:
                    sub_total += 1
                    right += 1
                total += sub_total
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
            for n in range(l, r+1):
                nums[n] = tmp[n]
            return total

        def divide(l: int, r: int) -> int:
            if l == r:
                return 0
            mid = l+(r-l)//2
            return divide(l, mid) + divide(mid+1, r) + merge(l, mid, r)
        
        return divide(0, length_-1)
# @lc code=end
