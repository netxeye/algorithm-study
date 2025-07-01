#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tree import TreeNode
from typing import Optional, List
from collections import deque


def breadth_first_search(root: Optional[TreeNode]) -> List[int]:
    "Also named as level-order-traversal or BFS"
    queue: deque[TreeNode] = deque()
    # queue: List[TreeNode] = list()
    queue.append(root)
    result = []
    while queue:
        # deque is not equal to None
        node: TreeNode = queue.popleft()
        # node: TreeNode = queue.pop(0)
        result.append(node.value)
        if node.left:
            # node.left is not None
            queue.append(node.left)
        if node.right:
            # node.left is not None
            queue.append(node.right)
    return result


def depth_first_search(root: Optional[TreeNode], pre_order: List[int],
                       in_order: List[int],
                       post_order: List[int]) -> List[int]:
    """
    Also named dfs, it has three different types
    pre_order(root, left, right), in_order(left, root, right),
    post_order(left, right, root)
    """
    if root is None:
        return
    pre_order.append(root.value)
    depth_first_search(root.left, pre_order, in_order, post_order)
    in_order.append(root.value)
    depth_first_search(root.right, pre_order, in_order, post_order)
    post_order.append(root.value)
    return pre_order, in_order, post_order


def depth_first_search2(root: Optional[TreeNode], pre_order: List[int],
                        in_order: List[int],
                        post_order: List[int]) -> list[int]:
    """
    Not use resution for dfs
    """
    stack: List[TreeNode] = []
    post_stack: List[TreeNode] = []
    stack.append(root)
    # post_order
    while stack:
        node: TreeNode = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        post_stack.append(node)
    while post_stack:
        node: TreeNode = post_stack.pop()
        post_order.append(node.value)
    stack.append(root)
    # pre_order
    while stack:
        node: TreeNode = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        pre_order.append(node.value)
    # in_order
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
            # put all left into stack
        curr = stack.pop()
        in_order.append(curr.value)
        curr = curr.right
    return pre_order, in_order, post_order


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    #    n1
    #    /\
    #  n2  n3
    #  /\
    # n4 n5
    bfs = breadth_first_search(n1)
    dfs_pre, dfs_in, dfs_post = depth_first_search(n1, [], [], [])
    print(bfs)
    print("level-order traversal should be [1,2,3,4,5]")
    print(f"{bfs} == [1,2,3,4,5], the result is {bfs == [1, 2, 3, 4, 5]}")
    print(dfs_pre)
    print("pre-order traversal should be [1,2,4,5,3]")
    print(f"{dfs_pre} == [1,2,4,5,3], ",
          f"the result is {dfs_pre == [1, 2, 4, 5, 3]}")
    print(dfs_in)
    print("in-order traversal should be [4,2,5,1,3]")
    print(f"{dfs_in} == [4,2,5,1,3], ",
          f"the result is {dfs_in == [4, 2, 5, 1, 3]}")
    print(dfs_post)
    print("post-order traversal should be [4,5,2,3,1]")
    print(f"{dfs_post} == [4,5,2,3,1], ",
          f"the result is {dfs_post == [4, 5, 2, 3, 1]}")
    dfs_pre2, dfs_in2, dfs_post2 = depth_first_search2(n1, [], [], [])
    print(dfs_pre2)
    print("pre-order traversal should be [1,2,4,5,3] (non-recursive)")
    print(f"{dfs_pre2} == [1,2,4,5,3], ",
          f"the result is {dfs_pre2 == [1, 2, 4, 5, 3]}")
    print(dfs_in2)
    print("in-order traversal should be [4,2,5,1,3] (non-recursive)")
    print(f"{dfs_in2} == [4,2,5,1,3], ",
          f"the result is {dfs_in2 == [4, 2, 5, 1, 3]}")
    print(dfs_post2)
    print("post-order traversal should be [4,5,2,3,1] (non-recursive)")
    print(f"{dfs_post2} == [4,5,2,3,1], ",
          f"the result is {dfs_post2 == [4, 5, 2, 3, 1]}")
