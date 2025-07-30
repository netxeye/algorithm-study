#! /usr/bin/env python3
# -*-coding: utf-8 -*-
from random import randint
from time import time


def merge_sort(arr: list[int]) -> list[int]:
    """
    归并排序, 把一个数组分成左右两个, 向下递归, 递归深度是 log N
    当递到只有一个元素的数组, 就认为这数组右序, 开始归,
    归的时候会有左右两个数组, 这两个数组会在归的时候进行合并排序
    这个时候递归栈的深度是 logN, 合并的时候需要划分一个新的列表,
    这个列表最大是 O(N), 所以空间是 O(N)+O(logN) ~= O(N)
    时间是 O(NlogN)
    """

    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    tmp_arr = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            tmp_arr.append(left_arr[i])
            i += 1
        else:
            tmp_arr.append(right_arr[j])
            j += 1
    tmp_arr.extend(left_arr[i:])
    tmp_arr.extend(right_arr[j:])
    return tmp_arr


def merge_sort2(arr: list[int]) -> list[int]:
    """
    非递归排序:
    使用步长 step = 1 开始,每次步长翻倍 step<<=1
    这样就会有左右两个 sub_arr
    left, right = arr[:mid], arr[mid:]
    然后写会原来数组的位置
    """

    n = len(arr)
    step = 1
    while step < n:
        for start in range(0, n, step*2):
            # 如果步长是 1, 那么 start = 0, 1, 2, ..., n-1
            # 下面的是错误的
            # end = start + step
            # mid = start + (end-start)//2
            # 原因
            mid = min(start + step, n)
            # 中点不能超过 n, start + step 就是从 start
            # 到一个步长 step
            end = min(start + step * 2, n)
            # end 不能超过 n, start + step * 2
            # 就是从 start 到一个步长 step*2
            left = arr[start:mid]
            right = arr[mid:end]
            i = j = 0
            k = start
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left) and k < end:
                arr[k] = left[i]
                k += 1
                i += 1
            while j < len(right) and k < end:
                arr[k] = right[j]
                j += 1
                k += 1
        step <<= 1
    return arr


def merge_sort3(arr: list[int]) -> list[int]:
    """
    AI写的另外一个, 使用双缓冲方法
    """

    n = len(arr)
    if n == 0:
        return arr
    tmp = [None] * n
    step = 1
    while step < n:
        for start in range(0, n, step * 2):
            mid = min(start+step, n)
            end = min(start+step*2, n)
            i, j, k = start, mid, start
            while i < mid and j < end:
                if arr[i] <= arr[j]:
                    tmp[k] = arr[i]
                    i += 1
                else:
                    tmp[k] = arr[j]
                    j += 1
                k += 1
            while i < mid:
                tmp[k] = arr[i]
                i += 1
                k += 1
            while j < end:
                tmp[k] = arr[j]
                j += 1
                k += 1
        arr, tmp = tmp, arr
        step <<= 1
    return arr


if __name__ == "__main__":
    total_time = total_time2 = total_time3 = 0
    for i in range(1000):
        length = randint(1, 1000)
        arr = [randint(-1000, 1000) for _ in range(length)]
        arr1 = arr.copy()
        arr2 = arr.copy()
        arr3 = arr.copy()
        # 使用不同的函数进行排序, 并且测试时间
        t1 = time()
        sorted_arr = merge_sort(arr1)
        total_time += time() - t1
        t2 = time()
        sorted_arr2 = merge_sort2(arr2)
        total_time2 += time() - t2
        t3 = time()
        sorted_arr3 = merge_sort3(arr3)
        total_time3 += time() - t3

        if sorted_arr != sorted(arr):
            print(f"Test failed for array: {arr}")
            break
        if sorted_arr2 != sorted(arr):
            print(f"Test failed for arr: {arr} in merge_sort2")
            break
        if sorted_arr3 != sorted(arr):
            print(f"Test failed for arr: {arr} in merge_sort3")
            break
    else:
        print(f"merge_sort took {total_time:.6f} seconds",
              f"average {total_time/1000:.6f} seconds")
        print(f"merge_sort2 took {total_time2:.6f} seconds",
              f"average {total_time2/1000:.6f} seconds")
        print(f"merge_sort3 took {total_time3:.6f} seconds",
              f"average {total_time3/1000:.6f} seconds")
        print("All tests passed!")
