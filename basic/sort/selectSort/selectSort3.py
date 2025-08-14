#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


def select_sort(nums: list[int]) -> list[int]:
    """
    There is two areas, the front area is sorted area
    The area next to sorted area is unsorted area
    There is two pointers, one is point to the next of element
    which is last element of sorted area. Another pointer
    point to the smallest element in the unsorted area.
    And then, switch two pointers' element. the next of element
    which is last element of sorted area move forward by one.
    Repeat above steps
    """
    n = len(nums)
    for i in range(n):
        # the first pointer
        smallest = i
        for j in range(i+1, n):
            # smallest pointer
            if nums[smallest] > nums[j]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums


if __name__ == "__main__":
    for i in range(1000):
        length = randint(1, 1000)
        arr = [0] * length
        for j in range(length):
            arr[j] = randint(-1000, 1000)
        if select_sort(arr[:]) != sorted(arr):
            print("Error")
            print(arr)
            break
    else:
        print("works")
