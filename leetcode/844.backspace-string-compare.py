#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        skip_s, skip_t = 0, 0
        n_s, n_t = len(s)-1, len(t)-1
        while n_s >=0 and n_t >= 0:
            while skip_s > 0 or s[n_s] == '#':
                skip_s = skip_s+1 if s[n_s] == '#' else skip_s-1
            while skip_t > 0 or t[n_t] == '#':
                skip_t = skip_t+1 if s[n_t] == '#' else skip_t-1
            if s[n_s] != t[n_t]:
                return False
        return True

        
# @lc code=end