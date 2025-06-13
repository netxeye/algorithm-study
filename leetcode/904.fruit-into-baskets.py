#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#
from typing import List
# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, n, basket = 0, len(fruits), dict()
        max_tree = 0
        for r in range(n):
            basket[fruits[r]] = r # save the lastest index of the type of fruit
            if len(basket) > 2: # basket has more than two type of fruits
                # find the most left fruit. the third fruit is added from above code
                # therefore, the another two fruits in the basket has smaller index
                # we need to find the most left fruit which is the smallest index
                # in the basket
                min_index = min(basket.values())# Time: O(K), K is the basket size
                # K will be 1~3. O(3) can be simplify as O(1)
                basket.pop(fruits[min_index]) # remove the most left fruit from basket
                l = min_index+1 # move the left pointer of silding window to reminding fruit's frist index
            max_tree = max(max_tree, r-l+1) # after the if block, the silding window is [l,r] which l and r both are vaildate index
        return max_tree

# @lc code=end

