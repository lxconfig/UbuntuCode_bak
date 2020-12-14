

"""
    给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
"""


class Solution:
    def maxProfit(self, maxK: int, prices: list) -> int:
        """动态规划
        跟之前分析的一致，不同的是此题k的大小会是任意的数字，要对k这个状态进行穷举
        状态方程依旧是：
            dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
            dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        """
        # prices数组很大时，dp数组太大会超时
        # if not prices: return 0
        # n = len(prices)
        # dp = [ [[0] * 2 for _ in range(maxK+1)] for _ in range(n) ]

        # for i in range(n):
        #     for k in range(maxK, 0, -1):
        #         if i == 0:
        #             dp[i][k][0], dp[i][k][1] = 0, -prices[i]
        #         else:
        #             dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        #             dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        # return dp[n-1][maxK][0]

        if not prices: return 0
        n = len(prices)
        # k应该不超过n/2，如果超过，就没有限制，就等同于k无穷大的情况
        if maxK > n // 2:
            return self.maxProfit_inf_k(prices)
        
        dp = [ [[0] * 2 for _ in range(maxK+1)] for _ in range(n) ]
        for i in range(n):
            for k in range(maxK, 0, -1):
                if i == 0:
                    dp[i][k][0], dp[i][k][1] = 0, -prices[i]
                else:
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[n-1][maxK][0]


    def maxProfit_inf_k(self, prices: list) -> int:
        """动态规划-空间优化版
        """
        if not prices: return 0
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -prices[0]
        for i in range(1, n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0

if __name__ == "__main__":
    s = Solution()
    prices = [3,2,6,5,0,3]
    print(s.maxProfit(2, prices))