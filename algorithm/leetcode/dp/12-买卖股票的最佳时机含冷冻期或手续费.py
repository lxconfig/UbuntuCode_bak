


class Solution:
    def maxProfitWithCoolDown(self, prices: list) -> int:
        """动态规划-含冷冻期
        给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
        设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
            你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
            卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

        根据之前的分析，可以写出状态转移方程：
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])  由于含冷静期，所以买的时候，不能是前一天(i-1)，要前两天(i-2)
        """
        # if not prices: return 0
        # n = len(prices)
        # dp = [[0] * 2 for _ in range(n)]
        # for i in range(n):
        #     if i == 0:
        #         dp[i][0], dp[i][1] = 0, -prices[i]
        #     else:
        #         dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        #         dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        # return dp[n-1][0]
        if not prices: return 0
        n = len(prices)
        dp_i_0, dp_i_1, dp_pre_0 = 0, -prices[0], 0  # dp_pre_0表示dp[i-2][0]
        for i in range(1, n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp
        return dp_i_0
    

    def maxProfitWithFee(self, prices: list, fee: int) -> int:
        """动态规划-含手续费
        给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
        你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。返回获得利润的最大值。

        根据之前的分析，可以写出状态转移方程：
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)  相当于卖出的时候利润减少了，再下面的式子里减去fee也可以
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]) 
        """
        # if not prices: return 0
        # n = len(prices)
        # dp = [[0] * 2 for _ in range(n)]
        # for i in range(n):
        #     if i == 0:
        #         dp[i][0], dp[i][1] = 0, -prices[i]
        #     else:
        #         dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
        #         dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        # return dp[n-1][0]
        if not prices: return 0
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -prices[0]
        for i in range(1, n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0


if __name__ == "__main__":
    s = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    print(s.maxProfitWithFee(prices, 2))