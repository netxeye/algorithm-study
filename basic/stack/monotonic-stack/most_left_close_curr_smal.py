#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def most_left_closed_curr_smal(arr: List[int]) -> list[int]:
    '''
    Return the indeices of input array which indicates
    the first element smaller than the current element on the left
    which closed to current element
    '''
    n = len(arr)
    ans = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[i] <= arr[stack[-1]]:
            ans[stack.pop()] = stack[-1]
        stack.append(i)
    return ans


if __name__ == '__main__':
    # Test cases
    print(most_left_closed_curr_smal([9, 2, 4, 12, 10, 8, 1, 6]))
