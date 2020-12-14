

"""
    给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
"""



class Solution:
    def maxProfit(self, prices: list) -> int:
        """动态规划
        跟前面分析不同的是，此题限定k=2，所以不能忽略掉k这个状态
        状态方程依旧是：
            dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
            dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        全部列举出来：
            dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
            dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])

            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i])
                        = max(dp[i-1][1][1], -prices[i])
            
        """
        # if not prices: return 0
        # n = len(prices)
        # dp = [ [[0] * 2 for i in range(3)] for i in range(n) ]  # 3行2列，z=n的三维数组
        # for i in range(n):
        #     for k in range(2, 0, -1):
        #         if i == 0:
        #             dp[i][k][0], dp[i][k][1] = 0, -prices[i]
        #         else:
        #             dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        #             dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
                    
        # return dp[n-1][2][0]
        
        if not prices: return 0
        n = len(prices)
        # i就理解为0
        dp_i20, dp_i21 = 0, -prices[0]
        dp_i10, dp_i11 = 0, -prices[0]

        for i in range(1, n):
            # for k in range(2, 0, -1):
            dp_i20 = max(dp_i20, dp_i21 + prices[i])
            dp_i21 = max(dp_i21, dp_i10 - prices[i])
            dp_i10 = max(dp_i10, dp_i11 + prices[i])
            dp_i11 = max(dp_i11, -prices[i])
        return dp_i20


if __name__ == "__main__":
    s = Solution()
    prices = [3,3,5,0,0,3,1,4]
    print(s.maxProfit(prices))