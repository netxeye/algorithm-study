#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


def quickSort(nums: list[int], left: int, right: int) -> list[int]:
    """
    Quick Sort need partition to find index
    of pivot:
    1. pick a element as pivot
    2. have two pointer: left and right
    3. first from right to left to find the first
       element smaller than pivot
    4. after that from left to right to find
       the first element bigger than pivot
    5. switch the step 3 element and step 4 element
    6. repeat step 3-5 until left and right meet(left == right)
    7. switch the pivot and left
    8. return pivot new index(pointer left)
    after find the pivot, recucious quick sort:
    1. quick sort [left, pivot]
    2. quick sort [pivot+1, right]
    """
    if left >= right:
        return
    pivot = partition(nums, left, right)
    quickSort(nums, left, pivot-1)
    quickSort(nums, pivot+1, right)


def partition(nums: list[int], left: int, right: int) -> int:
    "partition"
    pick = randint(left, right)
    nums[left], nums[pick] = nums[pick], nums[left]
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1
        while i < j and nums[i] <= nums[left]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i], nums[left] = nums[left], nums[i]
    return i


if __name__ == "__main__":
    for _ in range(1000):
        length = randint(1, 1000)
        arr = [randint(-1000, 1000) for _ in range(length)]
        arr_copy = arr[:]
        quickSort(arr, 0, length-1)
        if sorted(arr_copy) != arr:
            print(f"Error, {arr}\n, {quickSort(arr[:], 0, len(arr)-1)}")
            break
    else:
        print("Works")
