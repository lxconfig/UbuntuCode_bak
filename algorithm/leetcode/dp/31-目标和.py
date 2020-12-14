
"""
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums: return 0
        nums_sum = sum(nums)
        if nums_sum < S: return 0
        capacity = (S + nums_sum) // 2
        if (S + nums_sum) % 2 == 1:
            return 0
        size = len(nums)
        dp = [[0 for _ in range(capacity + 1)] for _ in range(size + 1)]
        dp[0][0] = 1
        for i in range(1, size + 1):
            for j in range(capacity + 1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] +  dp[i - 1][j - nums[i - 1]]
        print(dp)
        return dp[size][capacity]


if __name__ == "__main__":
    s = Solution()
    nums, S = [1,1,1,1,1], 3
    print(s.findTargetSumWays(nums, S))