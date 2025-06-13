#
# @lc app=leetcode id=707 lang=python3
# @lcpr version=30200
#
# [707] Design Linked List
#
from typing import Optional

# @lc code=start
class LinkedNode:

    def __init__(self, val: int=0, prev: Optional['LinkedNode']=None, next: Optional['LinkedNode']=None ) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = LinkedNode()
        self.size = 0
        self.tail = self.head

    # query
    def get(self, index: int) -> int:
        "Query the value of indexTH node"
        if not self.isAvailableIndex(index):
            return -1
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val
    
    def getSize(self) -> int:
        return self.size
    
    def getHead(self) -> Optional[LinkedNode]:
        return self.head
    
    def getTail(self) -> Optional[LinkedNode]:
        return self.tail
        
    # add
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if not self.isPossibleIndex(index):
            return
        prev = self.head
        for _ in range(index):
            prev = prev.next
        newNode = LinkedNode(val, prev, prev.next)
        prev.next = newNode
        if index == self.size:
            self.tail = newNode
        else:
            prev.next.prev = newNode
        self.size += 1
        
    # delete
    def deleteAtIndex(self, index: int) -> None:
        if not self.isAvailableIndex(index):
            return
        prev = self.head
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        if index == self.size-1:
            self.tail = prev
        else:
            prev.next.prev = prev
        self.size -= 1

    def deleteAtHead(self) -> None:
        self.deleteAtIndex(0)
    
    def deleteAtTail(self) -> None:
        self.deleteAtIndex(self.size-1)
        
    # check
    def isAvailableIndex(self, index: int) -> bool:
        "Check the index is in the range"
        return 0 <= index < self.size

    def isPossibleIndex(self, index: int) -> bool:
        "Check is the index can be used for adding new node"
        return 0 <= index <= self.size


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end



