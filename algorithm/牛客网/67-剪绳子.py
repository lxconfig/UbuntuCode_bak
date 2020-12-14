


"""
    给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。
    请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
"""


class Solution:
    def cutRope(self, number):
        """动态规划
        不论怎么切割绳子，肯定有一个划分点，把绳子分成两段，那么这两段绳子又构成原问题的子问题
        两段绳子最大乘积的乘积，就是原问题的解
        设划分点为i，dp[i]表示长度为i的绳子的最大乘积
        则转移方程为:
            dp[i] = max(dp[i], dp[j] * dp[i-j])  0 < j < i
        其中，j表示划分的两段绳子中一段绳子的长度，那么另一段绳子的长度就是i-j
        """
        # 运行时间：33ms  占用内存：5844k
        if number == 0:
            return 0
        dp = [0] * (number + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, number+1):
            if i == number:
                dp[i] = 1
            else:
                dp[i] = i
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * dp[i-j])
        
        return dp

    def cutRope2(self, number):
        # 运行时间：25ms  占用内存：5864k
        if number == 2:
            return 1
        if number == 3:
            return 2
        x = number % 3
        y = number // 3
        if x == 0:
            return pow(3, y)
        elif x == 1:
            return 2 * 2 * pow(3, y - 1)
        else:
            return 2 * pow(3, y)


if __name__ == "__main__":
    solution = Solution()
    print(solution.cutRope2(8))        