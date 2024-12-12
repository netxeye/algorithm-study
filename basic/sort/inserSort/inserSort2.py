#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# 插入排序练习
# 插入排序和打扑克一样。现保证0～0有序，相当手上有第一张牌，本身就有序
# 然后0～1有序，这时候等于从列表后面拿到第一张牌，和手上的牌形成了2张。如果1号牌大就放在0号的后面
# 然后0～2有序，大的牌和0～1的牌挨个比较，直到放到有序的位置

# 引入random 的库，为实现对数器
import random
# 引入typting，实现声明类型
from typing import List


def randomArray(maxLan: int, maxVal: int) -> List[int]:
    "生成随机数组，变量都是左闭右开的右开部分"
    arr = list()
    for i in range(random.randint(0, maxLan-1)):
        arr.append(random.randint(0, maxVal-1))
    return arr


def compareArr(arr1: List[int], arr2: List[int]) -> bool:
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


def inserSort1(arr: List[int]) -> List[int]:
    """
    使用插入的方式
    """
    for i in range(1, len(arr)):
        current_value = arr[i]
        prev_indx = i - 1
        while prev_indx >= 0 and arr[prev_indx] > current_value:
            arr[prev_indx + 1] = arr[prev_indx]
            prev_indx -= 1
        arr[prev_indx + 1] = current_value
    return arr


def inserSort2(arr: List[int]) -> List[int]:
    """
    这个交换的方式，性能比较差，但是我自己想的
    """
    # 设立边界，arr长度为零或者null，或者就一个element
    # if len(arr) in (0, 1):
    #     return arr
    # 下面的循环包含了上面的边界
    # 从1开始，默认0是有序
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                tmp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = tmp
    return arr


if __name__ == "__main__":
    for i in range(5000):
        arr = randomArray(1000, 50000)
        arr1 = inserSort1(arr)
        arr2 = sorted(arr)
        if not compareArr(arr1, arr2):
            print("Error")
            print("arr1 use my fun: \n", arr1)
            print("arr2 use sorted()\n:", arr2)
            print("original:\n", arr)
            break
    print(compareArr(arr1, arr2))
