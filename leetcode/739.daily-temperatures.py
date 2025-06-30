#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                curr_temper = stack.pop()
                ans[curr_temper] = i - curr_temper
            stack.append(i)
        return ans
# @lc code=end