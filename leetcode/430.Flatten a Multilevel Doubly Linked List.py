#
# @lc app=leetcode id=430 lang=python3
# @lcpr version=30200
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

