#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, n, sub_str, longest = 0, len(s), set(), 0
        for r in range(n):
            # Find the duplicated chart
            while s[r] in sub_str:
                sub_str.remove(s[l])# remove the left pointer
                l += 1
             # after the while [l,r-1](sub_str) does not include current r chart
            sub_str.add(s[r]) # add new chart
            longest = max(longest, r-l+1) # [l,r] is substring without repeating chart
        return longest


# @lc code=end

