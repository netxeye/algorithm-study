#
# @lc app=leetcode id=201 lang=python3
# @lcpr version=30100
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 每次对比总会得到更小的一个数. 这样可以从右边开始做 bitwise and 运算
        # 一旦得到的数比 right 小, 那么就可以停止了
        while right > left:
            right &= right - 1
        return right & left
    
    def rangeBitwiseAnd2(self, left: int, right: int) -> int:
        shift = 0
        while right != left:
            right >>= 1
            left >>= 1
            shift += 1
        return right << shift