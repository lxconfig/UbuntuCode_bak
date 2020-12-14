

"""
    给定一个数组，表示每天的股票价格，问如果能得到最大利润

    思路：先找到最小的买入价格，在和之后的价格比较，得出最大利润
"""

# O(n)  time
# O(1)  space
def MaxProfit(array):
    if len(array) < 2:
        return 0
    profit = 0
    min_buy_value = array[0]
    for i in range(1, len(array)):
        if array[i] < min_buy_value:
            # 找最小的买入价格
            min_buy_value = array[i]
        # 计算之前最大的利润，和当前卖出价格-最小买入价格的利润大小
        profit = max(profit, array[i] - min_buy_value)
    return profit


# O(n)  time
# O(n)  space
def MaxProfitDP(array):
    n = len(array)
    if n < 2:
        return 0
    dp = [0] * n
    min_buy_value = array[0]
    for i in range(1, n):
        min_buy_value = min(array[i], min_buy_value)
        dp[i] = max(array[i] - min_buy_value, dp[i-1])
    return dp



def pro_stock_prob(array, k):
    """可以进行任意多次的交易，但是每次卖出的时候要缴纳手续费k元。求最大利润
    记：当天有两种状态：hold(持有股票)  cash(持有现金)
    设：第1天买了股票，是hold状态 hold[0] = -array[0]，无现金 cash[0] = 0
    若：第2天是hold，有两种情况：
        (1) 第1天就hold，第2天没有做操作，则 hold[1] = hold[0]
        (2) 第1天是cash，第2天买入了股票，则 hold[1] = cash[0] - array[1]
        第2天hold[1] = max(hold[0], cash[0] - array[1])
    第2天是cash，也有两种情况：
        (1) 第1天是cash，第2天没有做操作，则 cash[1] = cash[0]
        (2) 第1天是hold，第2天卖掉了股票，则 cash[1] = hold[0] + array[1] - k
        第2天cash[1] = max(cash[0], hold[0] + array[1] - k)
    
    所以： 第i天： cash[i] = max(cash[i-1], hold[i-1] + array[i] - k)
                  hold[i] = max(hold[i-1], cash[i-1] - array[i])
    """
    n = len(array)
    if n < 2:
        return 0
    # hold, cash = [-array[0]] * n, [0] * n  # O(n)  space
    hold, cash = -array[0], 0
    for i in range(1, n):
        # hold[i] = max(hold[i-1], cash[i-1] - array[i])
        # cash[i] = max(cash[i-1], hold[i-1] + array[i] - k)
        
        hold = max(hold, cash - array[i])
        cash = max(cash, hold + array[i] - k)

    # return max(hold[-1], cash[-1])
    return max(hold, cash)


if __name__ == "__main__":
    array = [1,3,2,8,4,9]
    # print(MaxProfitDP(array))
    print(pro_stock_prob(array, 2))