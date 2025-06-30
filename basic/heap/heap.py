#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Heap:
    def __init__(self):
        self.heapSize = 0
        self.data = []

    def heapify(self, i=0):
        while i < self.heapSize:
            l = i*2 +1
            r = i*2 +2
            largest = i
            largest = l if l < self.heapSize and self.data[l] > self.data[largest] else
            largest
            largest = r if r < self.heapSize and self.data[r] > self.data[largest] else
            largest
            if largest != i:
                self.data[i], self.data[largest] = self.data[largest], self.data[i]
            else:
                break

