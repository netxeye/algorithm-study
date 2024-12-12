#! /usr/bin/env python
# -*- coding: utf-8 -*-
##
# instertionSort 和instertionSort2的区别是，前者是将当前值赋给current，后者是直接交换值
# 两种方式的结果是一样的
# 两种方式的时间复杂度都是O(n^2)

def insertionSort(arr: list) -> list:
    print("Start arr: ", arr)
    for i in range(1, len(arr)):
        print("step: 1")
        print("preIndex: ", i - 1)
        preIndex = i - 1
        print("current: ", arr[i])
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            print("step: 2 in the while loop")
            arr[preIndex + 1] = arr[preIndex]
            print("arr[preIndex + 1]: ", arr[preIndex + 1])
            print("arr[preIndex]: ", arr[preIndex])
            print("arr: ", arr)
            preIndex -= 1
            print("preIndex: ", preIndex)
        print("step: 3 out of the while loop, swap the current value")
        arr[preIndex + 1] = current
        print("arr[preIndex + 1]: ", arr[preIndex + 1])
        print(arr)
    return arr


def insertionSort2(arr: list) -> list:
    print("Start arr:", arr)
    for i in range(1, len(arr)):
        print("step: 1")
        preIndex = i - 1
        while preIndex >= 0 and arr[preIndex] > arr[preIndex + 1]:
            tmp = arr[preIndex]
            arr[preIndex] = arr[preIndex + 1]
            arr[preIndex + 1] = tmp
            preIndex -= 1
    return arr


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 1]
    print(insertionSort(arr))
