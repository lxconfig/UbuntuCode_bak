

"""
    给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        size, weight = len(nums), sum(nums)
        # 和为奇数，肯定不能分割
        if weight % 2 == 1:
            return False
        else:
            weight //= 2
        dp = [[False for _ in range(weight+1)] for _ in range(size+1)]
        # base case
        for i in range(size+1):
            dp[i][0] = True
        
        for i in range(1, size + 1):
            for j in range(1, weight + 1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
        return dp[size][weight]

    def canPartition_1(self, nums: List[int]) -> bool:
        """空间优化
        """
        size, weight = len(nums), sum(nums)
        # 和为奇数，肯定不能分割
        if weight % 2 == 1:
            return False
        else:
            weight //= 2
        dp = [False for _ in range(weight+1)]
        # base case
        dp[0] = True
        for i in range(1, size + 1):
            for j in range(weight, -1, -1):
                if j - nums[i - 1] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i - 1]]
        return dp[weight]


if __name__ == "__main__":
    s = Solution()
    nums = [1,2, 5]
    print(s.canPartition_1(nums))