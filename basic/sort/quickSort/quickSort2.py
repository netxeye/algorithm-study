#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


def find_mid(nums: list[int], left: int, mid: int, right: int) -> int:
    """find the new pick index by compared left, mid and right values"""
    l, m, r = nums[left], nums[mid], nums[left]
    if (l <= m <= r) or (r <= m >= l):
        return mid
    elif (m <= l <= r) or (r <= l <= m):
        return left
    else:
        return right


def partition(nums: list[int], left: int, right: int) -> int:
    """find the pivot"""
    pick_mid: int = find_mid(nums, left, left+(right-left)//2, right)
    nums[left], nums[pick_mid] = nums[pick_mid], nums[left]
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1
        while i < j and nums[i] <= nums[left]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i], nums[left] = nums[left], nums[i]
    return i


def quick_sort(nums: list[int], left: int, right: int):
    """
    在某些输入下，快速排序可能占用空间较多。以完全有序的输入数组为例，设递归中的子数组长度为
    `m-1` ，每轮哨兵划分操作都将产生长度为 `0`的左子数组和长度为 `m-1`的右子数组，这意味着每
    一层递归调用减少的问题规模非常小（只减少一个元素），递归树的高度会达到 `m-1`，此时需要占
    用`O(n)`大小的栈帧空间。为了防止栈帧空间的累积，我们可以在每轮哨兵排序完成后，比较两个子
    数组的长度，仅对较短的子数组进行递归。由于较短子数组的长度不会超过`n/2`，因此这种方法能
    确保递归深度不超过`O(logn)`，从而将最差空间复杂度优化至`O(logn)`
    """
    while left < right:
        pivot = partition(nums, left, right)
        if pivot - left < right - pivot:
            quick_sort(nums, left, pivot-1)
            left = pivot + 1
        else:
            quick_sort(nums, pivot+1, right)
            right = pivot - 1


if __name__ == "__main__":
    for _ in range(1000):
        length: int = randint(1, 1000)
        arr: list[int] = [randint(-1000, 1000) for _ in range(length)]
        arr_copy: list[int] = arr[:]
        quick_sort(arr, 0, length-1)
        if sorted(arr_copy) != arr:
            print(f"error, {arr}\n {arr_copy}")
            break
    else:
        print("works")
