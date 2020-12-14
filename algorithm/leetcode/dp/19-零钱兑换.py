

"""
    给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """暴力递归，会超时
        """
        if not coins: return 0
        size = len(coins)
        def dp(n):
            if n == 0: return 0
            elif n < 0: return -1
            res = float("inf")
            for i in range(size):
                subproblem = dp(n-coins[i])
                if subproblem == -1: continue
                res = min(res, subproblem + 1)
            return res if res != float("inf") else -1
        return dp(amount)

    def coinChange_1(self, coins: List[int], amount: int) -> int:
        """递归+备忘录
        """
        if not coins: return 0
        size = len(coins)
        memo = dict()
        def dp(n):
            if n in memo: return memo[n]
            if n == 0: return 0
            elif n < 0: return -1
            res = float("inf")
            for i in range(size):
                subproblem = dp(n-coins[i])
                if subproblem == -1: continue
                res = min(res, subproblem + 1)
            memo[n] = res if res != float("inf") else -1
            return memo[n]
        return dp(amount)

    def coinChange_2(self, coins: List[int], amount: int) -> int:
        if not coins: return 0
        # size = len(coins)
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], dp[i-coin] + 1)
        print(dp)
        return dp[-1] if dp[-1] != float("inf") else -1


if __name__ == "__main__":
    s = Solution()
    coins = [1, 2, 5]
    print(s.coinChange_2(coins, 5))