

"""
    一只青蛙一次可以跳上1级台阶，也可以跳上2级。
    求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

    f(n) = f(n-1) + f(n-2)

    运行时间：38ms
    占用内存：5812k
"""


class Solution:
    def jumpFloor(self, number):
        if number < 1:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            a, b, ret = 1, 2, 0
            for _ in range(3, number+1):
                a, b = b, a+b
                ret = b
            return ret


def climbingStairs(n):
    """使用动态规划的标准解法"""
    # f(n) = f(n-1) + f(n-2)
    dp = [None] * (n+1)
    dp[0] = dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


if __name__ == "__main__":
    solution = Solution()
    print(solution.jumpFloor(10))