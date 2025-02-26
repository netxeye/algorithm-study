#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Optional


class DoublyListNode(object):
    __slots__ = ("_val", "_next", "_prev")

    def __init__(self, val):
        self._val = val
        self._next = None
        self._prev = None

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, nextNode):
        self._next = nextNode

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prevNode):
        self._prev = prevNode


def createDoublyLinkedList(arr: List[int]) -> Optional[DoublyListNode]:
    if arr is None or len(arr) == 0:
        return None

    head = DoublyListNode(arr[0])
    cur = head

    for v in arr[1:]:
        newNode = DoublyListNode(v)
        cur.next = newNode
        newNode.prev = cur
        cur = cur.next

    return head


if __name__ == "__main__":
    head = createDoublyLinkedList([i for i in range(10)])

    # 打印都有的双链表的值
    cur = head
    while cur is not None:
        print(cur.val)
        cur = cur.next
