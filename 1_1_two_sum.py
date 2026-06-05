"""
https://leetcode.cn/problems/two-sum/description/?envType=study-plan-v2&envId=top-100-liked
1. 两数之和
提示
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]


提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案


进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
"""

from typing import List


## upgrade
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = sorted(nums)
        lens = len(nums)
        left = 0
        right = lens - 1
        ans = []
        while left < right:
            sum = new_nums[left] + new_nums[right]
            if sum == target:
                break
            elif sum < target:
                left += 1
            else:
                right -= 1
        for i in range(lens):
            if nums[i] == new_nums[left]:
                ans.append(i)
            elif nums[i] == new_nums[right]:
                ans.append(i)

        return ans
