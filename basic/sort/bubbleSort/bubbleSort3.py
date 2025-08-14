#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


def bubble_sort_with_flag(nums: list[int]) -> list[int]:
    n = len(nums)

    for j in range(n-1, 0, -1):
        flag = False
        for i in range(j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                flag = True
        if not flag:
            break
    return nums


if __name__ == "__main__":
    for _ in range(1000):
        length = randint(1, 1000)
        arr = [0] * length
        for i in range(length):
            arr[i] = randint(-1000, 1000)
        if bubble_sort_with_flag(arr[:]) != sorted(arr):
            print("ERR")
            print(arr, bubble_sort_with_flag(arr[:]), sorted(arr))
            break
    else:
        print("ok")
