#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


class LinkNode(object):
    __slots__ = ('_value', '_next')

    def __init__(self, v):
        self._value = v
        self._next = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, n):
        self._next = n


def createLinkedList(arr: List[int]) -> LinkNode:
    if arr is None or len(arr) == 0:
        return None

    head = LinkNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = LinkNode(arr[i])
        cur = cur.next

    return head


if __name__ == "__main__":
    head = createLinkedList([str(i) for i in range(20)])
    newHead = LinkNode(0)
    newHead.next = head
    head = newHead
    newTail = LinkNode(20)
    cur = head
    while cur.next is not None:
        cur = cur.next
    cur.next = newTail
    p = head
    while p is not None:
        print(p.value)
        p = p.next
