#
# @lc app=leetcode id=2 lang=python3
# @lcpr version=30200
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy head for the loop
        dummy_head = ListNode()
        # result head
        head = dummy_head
        # carry value if the total is more the 10
        carry, total = 0, 0
        while l1 is not None or l2 is not None or carry != 0:
            if l1 is not None:
                total += l1.val
                l1 = l1.next
            if l2 is not None:
                total += l2.val
                l2 = l2.next
            carry = total // 10
            new_node = ListNode(total%10)
            dummy_head.next = new_node
            dummy_head = new_node
            total = carry
        return head.next       
# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#

