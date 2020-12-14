

"""
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
"""


class Solution:
    def maxProfit(self, prices: list) -> int:
        """峰谷法
        连续的波谷和波锋之差相加，就是最大利润
        """
        if not prices: return 0
        n, i, profit = len(prices), 0, 0
        valley, peak = prices[0], prices[0]
        while i < n-1:
            while i < n-1 and prices[i] >= prices[i+1]: i += 1
            valley = prices[i]   # 找波谷
            while i < n-1 and prices[i] <= prices[i+1]: i += 1
            peak = prices[i]     # 找波峰
            profit += (peak - valley)
        
        return profit

    def maxProfit_1(self, prices: list) -> int:
        """
        只要后一天的价格比前一天大，就卖出，增加利润
        """
        if not prices: return 0
        n, profit = len(prices), 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
    
    def maxProfit_2(self, prices: list) -> int:
        """动态规划
        此题就是k=无穷大的情况，即不限制交易次数，此时k和k-1可以看作相等
        那么，根据前面的分析，状态转移方程为：
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        """
        if not prices: return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]

        for i in range(n):
            if i == 0:
                dp[i][0], dp[i][1] = 0, -prices[i]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        
        return dp[n-1][0]

    def maxProfit_3(self, prices: list) -> int:
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
    prices = [1,2,3,4,5]
    print(s.maxProfit_1(prices))
    print(s.maxProfit_2(prices))
    print(s.maxProfit_3(prices))