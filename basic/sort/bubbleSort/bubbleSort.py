#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# 学习冒泡排序，这个算法和气泡从水里升起
# 大的element会直接上升到最后一位。
# 这个过程是，比较一个index的数和它的下一位，如果前面的数小于后面的数，就前后交换。直到整个array
# 然后重复上吗的过程，不过因为最大的数被放到array的最后一位，所以每次循环都减少最后一位

# 引入random作为对数器来生成实验数据
from random import randint
# 引入typing作为记录paramater的类型
from typing import List


def randArray(maxLen: int, maxVal: int) -> List[int]:
    arr = list()
    for i in range(randint(0, maxLen)):
        arr.append(randint(0, maxVal))
    return arr


def compareArr(arr1: List[int], arr2: List[int]) -> bool:
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


def bubbleSort(arr: List[int]) -> List[int]:
    # 从开始interation到末尾
    length = len(arr)
    for j in range(1, length):
        for i in range(length-j):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
    return arr


if __name__ == "__main__":
    for i in range(50000):
        arr = randArray(100, 5000)
        arr1 = sorted(arr)
        arr2 = bubbleSort(arr)
        if not compareArr(arr1, arr2):
            print("Array arr2 is my algorithm: \n", arr2)
            print("Array arr1 is sorted(): \n", arr1)
            print("Array arr is orignal: \n", arr)
            print("Err: used the above information for debugging")
            break
    print(compareArr(arr1, arr2))
