

"""
    给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
"""
from typing import List



class Solution:
    def change_1(self, amount: int, coins: List[int]) -> int:
        size = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(size+1)]
        for i in range(size+1):
            dp[i][0] = 1
        print(dp)
        for i in range(1, size+1):
            for j in range(1, amount+1):
                if j - coins[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        print(dp)
        return dp[size][amount]

    def change_2(self, amount: int, coins: List[int]) -> int:
        """空间优化
        """
        size = len(coins)
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for i in range(size):
            for j in range(1, amount+1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j-coins[i]]
        return dp[amount]


if __name__ == "__main__":
    s = Solution()
    coins = [1, 2, 5]
    print(s.change_1(5, coins))