

"""
    假设每件珠宝的价值和重量都不一致，问在有限重量的背包中最多能装下多少价值的珠宝
"""


def knapSack(value, weight, back_weight):
    """二维动态规划
    设两个状态i,j，其中i表示前i个珠宝，j表示重量
    dp[i][j]表示在重量j的情况下，拿前i个珠宝时，能够获得的价值
    显然，dp[i][0] = 0
    先考虑i = 1时:
        dp[1][0] = 0
        dp[1][w1] = v1      如果j刚好就是第1个珠宝的重量，那么就可以获得它的价值v1
        dp[1][w] = 无穷大    对于其他重量，均不成立，认为是无穷大
    
    当i > 1时：
        dp[i][0] = 0
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-wi] + vi)
        dp[i-1][j]相当于不拿第i个珠宝，此时能获得的价值就是前面i-1个珠宝的价值
        dp[i-1][j-wi] + vi相当于拿第i个珠宝，那么就要留出第i个珠宝的重量(保证其一定能拿)，即前面i-1个珠宝的重量只有j-wi
    """
    dp = [[0 for i in range(back_weight + 1)] for j in range(len(value) + 1)]
    for i in range(len(value) + 1):
        for j in range(back_weight + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif weight[i-1] <= j:
                dp[i][j] = max(value[i-1] + dp[i-1][j-weight[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(value)][back_weight]


if __name__ == "__main__":
    value = [5, 7, 10, 13, 3, 11]
    weight = [2, 3, 4, 6, 1, 5]
    back_weight = 14
    print(knapSack(value, weight, back_weight))