"""
https://leetcode.cn/problems/subarray-sum-equals-k/description/?envType=study-plan-v2&envId=top-100-liked

560. 和为 K 的子数组

提示
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。



示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2


提示：

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 用于记录前缀和及其出现的次数，初始时前缀和0出现1次
        pre_sum_count = {0: 1}
        pre_sum = 0
        count = 0
        for num in nums:
            pre_sum += num
            # 查找是否存在前缀和为 pre_sum - k
            if pre_sum - k in pre_sum_count:
                count += pre_sum_count[pre_sum - k]
            # 更新当前前缀和出现的次数
            pre_sum_count[pre_sum] = pre_sum_count.get(pre_sum, 0) + 1
        return count
