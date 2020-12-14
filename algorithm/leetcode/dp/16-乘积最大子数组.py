
"""
    给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        size = len(nums)
        dp = [1] * size
        dp[0] = nums[0]
        for i in range(1, size):
            dp[i] = max(dp[i-1] * nums[i], nums[i])
        return max(dp)
    

    def maxProduct_1(self, nums: List[int]) -> int:
        """考虑了nums[i]正负情况的dp
        """
        if not nums: return 0
        size = len(nums)
        dp = [[0] * 2 for _ in range (size)]
        dp[0][1], dp[0][0] = nums[0], nums[0]
        for i in range(1, size):
            if nums[i] >= 0:
                dp[i][0] = min(dp[i-1][0] * nums[i], nums[i])
                dp[i][1] = max(dp[i-1][1] * nums[i], nums[i])
            else:
                dp[i][0] = min(dp[i-1][1] * nums[i], nums[i])
                dp[i][1] = max(dp[i-1][0] * nums[i], nums[i])
        
        # 遍历获取最大值
        res = dp[0][1]
        for i in range(1, size):
            res = max(dp[i][1], res)
        return res

    def maxProduct_2(self, nums: List[int]) -> int:
        if not nums: return 0
        size = len(nums)
        pre_max, pre_min, res = nums[0], nums[0], nums[0]
        for i in range(1, size):
            if nums[i] >= 0:
                cur_min = min(pre_min * nums[i], nums[i])
                cur_max = max(pre_max * nums[i], nums[i])
            else:
                cur_min = min(pre_max * nums[i], nums[i])
                cur_max = max(pre_min * nums[i], nums[i])
            res = max(res, cur_max)
            pre_max, pre_min = cur_max, cur_min
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [2,3,-2,4]
    print(s.maxProduct_2(nums))