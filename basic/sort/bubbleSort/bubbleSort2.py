#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from random import randint


def randArray(maxLen: int, maxVal: int) -> List[int]:
    arr = list()
    for n in range(randint(1, maxLen)):
        arr.append(randint(0, maxLen))
    return arr


def compareArry(arr1: List[int], arr2: List[int]) -> bool:
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


def bubbleSort(nums: List[int]) -> None:
    length_ = len(nums)
    for i in range(length_):
        for n in range(1, length_-i):
            if nums[n-1] > nums[n]:
                nums[n-1], nums[n] = nums[n], nums[n-1]


if __name__ == "__main__":
    for i in range(1000):
        arr = randArray(1000, 5000)
        arr1 = sorted(arr)
        bubbleSort(arr)
        print(i, end=" ")
        if not compareArry(arr1, arr):
            print("Err")
            break
    print(compareArry(arr1, arr))
