#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


def insert_sort(nums: list[int]) -> list[int]:
    """
    From unsorted area use the first unsorted element
    to compare with sorted area to find the correct plece.
    After found the correct place, from last element of
    sorted area, copy it value to next element until the
    right place. And then copy the value to correct index
    """
    n = len(nums)
    for i in range(1, n):
        # sorted area, start from [0,i-1]
        pick = nums[i]
        j = i-1
        while j >= 0 and nums[j] > pick:
            nums[j+1] = nums[j]
            j -= 1
        # j is the index of smaller than pick
        nums[j+1] = pick
    return nums


if __name__ == "__main__":
    for _ in range(1000):
        length = randint(1, 1000)
        arr = [randint(-1000, 1000) for _ in range(length)]
        if sorted(arr) != insert_sort(arr[:]):
            print(f"error, {insert_sort(arr[:])}")
            break
    else:
        print("Works")
