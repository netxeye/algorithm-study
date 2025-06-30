#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
from typing import List

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        # 先排序, Time: O(NlogN), 这样后面就能使用双指针的方式来根据结果移动左右指针, 从而找到正确结果gg
        # 因为要计算 4 个数的和, 这样我只需要遍历到倒数第 4 个就可以了
        for i in range(n-3):
            # 先固定住一个数字
            # 要求不能有重复, 这样需要向后查找重复
            if i > 0 and nums[i] == nums[i-1]:
                # 跳过第一个, 这样是为了向后去重, 所以检查 当前数字和他之前的一个数字是否相等
                continue
            # 现在的i index 的数字不是重复的了
            # 定位第二个数字
            for j in range(i+1,n-2):
                # 第二个固定的数字, 所以循环需要从第一个固定的数字 i 后面开始,
                # 因为第一个数字已经固定, 所以只需要找到剩下 2 个数字, 这样就不需要遍历所有,
                # 只需要遍历到倒数第三个数字
                # 第二个数字去重
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j+1, n-1
                total = nums[i] + nums[j]
                # 双指针模板
                while l < r:
                    # 剪枝
                    if nums[l] > 0 and total + 2 * nums[l] > target:
                        # 前两个固定数字和左指针指的剩下数字最小值
                        # 这样的4 sum 都大于 target,这样剩下不会有答案
                        # 这样做的前提是左指针是正数, 后面加不会越加越小
                        break
                    if nums[r] > 0 and total + 2 * nums[r] < target:
                        # 和上面同理
                        break
                    if total + nums[l] + nums[r] > target:
                        r -= 1
                    elif total + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        # 找到
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        # l去重
                        while l < r and nums[l] == nums[l+1]:
                            # 向前去重, 我们已经找到当前答案, 需要向前去重,找到同样值的最右边
                            l += 1
                        # r去重
                        while l < r and nums[r] == nums[r-1]:
                            # 向前去重, 因为是右指针, 移动方向是向左的, 相当于"向前"
                            r -= 1
                        # 现在 l 和r 都是重复数字的最后一位, 需要移动两个指正, 让遍历继续下去
                        l += 1
                        r -= 1
        return ans

        
# @lc code=end

