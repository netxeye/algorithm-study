#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from random import randint


def selectSort(nums: List[int]) -> None:
    length_ = len(nums)
    for i in range(length_):
        minValIndex = i
        for n in range(i, length_):
            if nums[n] < nums[minValIndex]:
                minValIndex = n
        nums[i], nums[minValIndex] = nums[minValIndex], nums[i]


def randArry(length: int, value: int) -> List[int]:
    arr = []
    for n in range(randint(1, length)):
        arr.append(randint(0, value))
    return arr


def isArryEqual(arr1: List[int], arr2: List[int]) -> bool:
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


if __name__ == "__main__":
    for i in range(1000):
        arr = randArry(5000, 50000)
        arr1 = sorted(arr)
        selectSort(arr)
        if not isArryEqual(arr1, arr):
            print("Err")
        print(i, end=" ")
    print("working")
