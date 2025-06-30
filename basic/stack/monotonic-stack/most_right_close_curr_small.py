#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def most_right_close_curr_samll(nums: List[int]) -> List[int]:
    """
    Return list of indices of input nums which indicates
    the index of samller number that is at right side of
    closest current element
    """
    n = len(nums)
    ans = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            ans[stack.pop()] = i
        stack.append(i)
    for i in range(n):
        while ans[i] != -1 and nums[i] == nums[ans[i]]:
            ans[i] = ans[ans[i]]
    return ans


if __name__ == "__main__":
    print(most_right_close_curr_samll([2, 6, 7, 2, 2, 1, 4, 0]))
