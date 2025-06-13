#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, n, sub_char_counter, longest, max_char_count = 0, len(s), dict(), 0, 0
        
        for r in range(n):
            sub_char_counter[s[r]] = sub_char_counter.get(s[r], 0) + 1
            max_char_count = max(max_char_count, sub_char_counter[s[r]])
            if (r-l+1) - max_char_count > k: # the sub-string nees more operations(k)
                sub_char_counter[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest
# @lc code=end
