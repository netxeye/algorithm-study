#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def mergeDivideConquer2(arr: list[int]) -> int:
    tmp = [0]*len(arr)

    def merge(left: int, mid: int, right: int) -> int:
        total = 0
        # 左右分别有序, 但是整体无序
        i = left
        sub_total = 0
        for j in range(mid+1, right+1):
            while i <= mid and arr[i] <= arr[j]:
                sub_total += arr[i]
                i += 1
            total += sub_total
        # mergeSort排序
        l_index, r_index, t_index = left, mid+1, left
        while l_index <= mid and r_index <= right:
            if arr[l_index] <= arr[r_index]:
                tmp[t_index] = arr[l_index]
                l_index += 1
            else:
                tmp[t_index] = arr[r_index]
                r_index += 1
            t_index += 1
        while l_index <= mid:
            tmp[t_index] = arr[l_index]
            t_index += 1
            l_index += 1
        while r_index <= right:
            tmp[t_index] = arr[r_index]
            t_index += 1
            r_index += 1
        for k in range(left, right+1):
            arr[k] = tmp[k]
        return total

    def smallSum(left: int,  right: int) -> int:
        # Only one element
        if right == left:
            return 0
        mid = left+(right-left)//2
        return smallSum(left, mid) + smallSum(mid+1, right) + merge(left, mid, right)
    return smallSum(0, len(arr)-1)


if __name__ == "__main__":
    arr = [5, 3, 4, 6, 1, 3, 2, 7, 1, 8]
    result = mergeDivideConquer2(arr)
    print("小合的和:", result)  # 输出小合的和
    print("排序后的数组:", arr)  # 输出排序后的数组
