#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# 选择排序：从左到右依次查找最小值的index。
# 然后吧最小值index下面的值和array的最左的值交换。然后从第二左的值开始重复
# 基本上就是每次循环都确保0～1， 0～2， 0～3 0～n-1,都是有序的

# 使用random来生成随机的array，用来做对数器
# randint(i,j) -> List[i,j] 一个左闭右闭的数组中的一个随机数
from random import randint
# 使用typing来标记paramaters
from typing import List


def randArr(maxLen: int, maxVal: int) -> List[int]:
    arr = list()
    for i in range(randint(1, maxLen)):
        arr.append(randint(0, maxVal))
    return arr


def isEqualArr(arr1: List[int], arr2: List[int]) -> bool:
    """
    比较两个array，如果两个的element相等就返回True，
    反之就返回False
    """
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


def selectSort(arr: List[int]) -> List[int]:
    copyArr = arr[:]
    length = len(arr)
    # for i in range(length):
    # 这里没有必要循环到最后一个element，到倒数第二个即可
    # 因为第二个循环用来寻找最小index的那个是从i+1开始，因此第一个循环可以从
    # lenght - 1结束
    for i in range(length-1):
        # 0 ~ end
        minValIndx = i
        for j in range(i+1, length):
            if copyArr[j] < copyArr[minValIndx]:
                minValIndx = j
        # 这里加一个判断，如果最小index和i相等，说明i就是最小index
        # 这样不需要交换，节约一次操作
        if minValIndx != i:
            copyArr[minValIndx], copyArr[i] = copyArr[i], copyArr[minValIndx]
    return copyArr


if __name__ == "__main__":
    for i in range(50000):
        arr = randArr(100, 5000)
        arr1 = selectSort(arr)
        arr2 = sorted(arr)
        result = isEqualArr(arr1, arr2)
        if not result:
            print("Arr1 is using my algorithm:\n", arr1)
            print("Arr2 is using sorted():\n", arr2)
            print("Arr is orginal:\n", arr)
            print("Err: use the aboved information for debugging")
            break
    print("Result is ", str(result).upper())
