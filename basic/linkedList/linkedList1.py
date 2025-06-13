#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.pre = None
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.pre = self.head

