#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# 归并分治:
# 1. 思考一个问题在大范围内上的答案, 是否等于, 左部分的答案 + 右部分的答案 +
# 跨越左右产生的答案.
# 2. 计算跨越左右产生的答案, 如果家还是那个左右各自右序, 会不会获得计算的便利性.
# 3. 如果以上两点都成立, 那么就可以使用归并分治.
# 4. 求解答案的过程只需要加入归并排序即可. 因为要让左右各自右序, 来获得计算的便利性.
# 求小合:
# 数组[5,3,4,6,1,3,2,7,1,8] 计算小合, 即每个数左边比它小的数的的和.
# index 0, 5, 小合为0
# index 1, 3, 小合为0. index 2, 4, 小合为0. index 3, 6, 小合为0.
# index 4, 1, 小合为0. index 5, 3, 小合为1. index 6, 2, 小合为4.
# index 7, 7, 小合为10. index 8, 1, 小合为0. index 9, 8, 小合为16.
# 最后返回这些小合的和. 这里需要考虑创建一个 def f(start, end). 这个 f会返回
# arry[start:end]的小合

def mergedDivideConquer(arr: list[int]) -> int:
    def merge(arr: list[int], left: int, right: int, mid: int) -> int:
        tmp = [0] * (right - left + 1)
        i = left
        j = mid+1
        k = total = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                tmp[k] = arr[i]
                total += arr[i]*(right-j+1)
                i += 1
            else:
                tmp[k] = arr[j]
                j += 1
            k += 1
        while i <= mid:
            tmp[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            tmp[k] = arr[j]
            j += 1
            k += 1
        # 写回去
        for idx in range(len(tmp)):
            arr[left+idx] = tmp[idx]
        return total

    def divide(arr: list[int], left: int, right: int) -> int:
        n = right - left + 1
        # [left, right]
        if n <= 1:
            return 0
        mid = left+(right-left) // 2
        l_total = divide(arr, left, mid)
        r_total = divide(arr, mid+1, right)
        cross_total = merge(arr, left, right, mid)
        return l_total + r_total + cross_total
    return divide(arr, 0, len(arr)-1)


if __name__ == "__main__":
    arr = [5, 3, 4, 6, 1, 3, 2, 7, 1, 8]
    result = mergedDivideConquer(arr)
    # assert result == 31, "小合的和应该是31"
    # 测试用例
    print("小合的和:", result)  # 输出小合的和
    print("排序后的数组:", arr)  # 输出排序后的数组
