#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random


def recur(n, total):
    # 使用尾部递归
    # 递归函数在返回的时候调用自身，并且return语句不能包含表达式
    if n == 0:
        return total
    else:
        return recur(n - 1, total + n)


def other(n):
    return n * (n + 1) // 2


if __name__ == "__main__":
    n = random.randint(1, 1000)
    for i in range(1, n):
        # assert recur(i) == other(i)
        if recur(i, 0) != other(i):
            print("error")
            break
    else:
        print("ok")
