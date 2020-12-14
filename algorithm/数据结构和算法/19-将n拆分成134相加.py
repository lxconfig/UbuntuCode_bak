"""
    给定n，找到不同的方法，将n写成1，3，4相加

    思路： 动态规划   f(n) = f(n-1) + f(n-3) + f(n-4)  n > 4
"""

import pysnooper


# @pysnooper.snoop()
def devide(n):
    dp = [None] * (n+1)
    dp[0] = dp[1] = dp[2] = 1
    dp[3] = 2
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-3] + dp[i-4]
    
    return dp[n]


if __name__ == "__main__":
    print(devide(6))