

"""
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
    注意：你不能在买入股票前卖出股票。
"""


class Solution:
    def maxProfit(self, prices: list) -> int:
        """动态规划
        先找到最小的买入价格，然后和当前价格相减，得出利润，再和之前的利润比较，得出最大利润
        dp[i]就表示第i天的利润
            dp[i] = max(prices[i] - min_buy_stock_value, dp[i-1])
        """
        if not prices: return 0
        n = len(prices)
        dp, min_buy_stock_value = [0] * n, prices[0]
        for i in range(1, n):
            min_buy_stock_value = min(prices[i], min_buy_stock_value)
            dp[i] = max(prices[i] - min_buy_stock_value, dp[i-1])
        return dp[n-1]


    def maxProfit_1(self, prices: list) -> int:
        """迭代
        """
        if not prices: return 0
        n, min_buy_stock_value, profit = len(prices), prices[0], 0
        for i in range(1, n):
            if prices[i] < min_buy_stock_value:
                min_buy_stock_value = prices[i]
            profit = max(prices[i] - min_buy_stock_value, profit)
        return profit


    def maxProfit_2(self, prices: list) -> int:
        """动态规划
        定义三种状态：
            - 天数i
            - 交易最大次数k
            - 当前是否持有股票，用1/0表示持有和不持有
        那么，能让三种状态互相转换的【选择】有三种：
            - 买
            - 卖
            - 无操作
        dp[i][k][1/0]就表示某一天的最大利润
        容易得出：
            dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
            dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        边界条件：
            dp[-1][k][0] = 0，因为天数从0-n，所以-1是非法的，自然最大利润就为0
            dp[-1][k][1] = 负无穷，因为天数不存在，又持有股票，用负无穷表示不可能
            dp[i][0][0] = 0，没有交易次数，自然最大利润就为0
            dp[i][0][1] = 负无穷，没有交易次数，不可能持有股票
        此题就是k=1的情况，带入上式，再结合边界条件化简可以得到状态转移方程：
            dp[i][1] = max(dp[i-1][1], -prices[i])
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        显然：
            dp[i][1] <= dp[i][0](卖出了股票肯定比还持有股票利润高)
        实际上：
            新的状态之和相邻的状态有关系，所以可以不用一个数组来存放所有状态
        """
        if not prices: return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            # 需要对i=0的情况进行特殊处理，因为i=0时，i-1=-1，会计算到最后一天的利润
            # 但这是不合法的，因此要特殊计算
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[n-1][0]

    def maxProfit_3(self, prices: list) -> int:
        """动态规划-空间优化
        """
        if not prices: return 0
        n = len(prices)
        # 定义边界条件，dp[0][0] = 0, dp[0][1] = -prices[i]
        dp_i_0, dp_i_1 = 0, -prices[0]
        for i in range(1, n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0



if __name__ == "__main__":
    s = Solution()
    prices = [3,3,5,0,0,3,1,4]
    print(s.maxProfit_3(prices))
