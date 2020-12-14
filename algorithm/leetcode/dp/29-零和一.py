
"""
"""


from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """三维动态规划
        没有进行状态压缩时，会超时
        """
        if not strs: return 0
        size = len(strs)
        # dp[i][m][n]
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(size + 1)]
        # base case 
        # 当i=0时，dp[0][m][n]=0
        for i in range(1, size + 1):
            # 先记录第i个字符串中0和1的数量
            count_0, count_1 = strs[i - 1].count("0"), strs[i - 1].count("1")
            # 穷举m和n
            for M in range(m + 1):
                for N in range(n + 1):
                    dp[i][M][N] = dp[i - 1][M][N]
                    if M >= count_0 and N >= count_1:
                        dp[i][M][N] = max(dp[i - 1][M][N], dp[i - 1][M - count_0][N - count_1] + 1)
        return dp[size][m][n]

    def findMaxForm_1(self, strs: List[str], m: int, n: int) -> int:
        """进行状态压缩
        """
        if not strs: return 0
        size = len(strs)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, size + 1):
            # 先记录第i个字符串中0和1的数量
            count_0, count_1 = strs[i - 1].count("0"), strs[i - 1].count("1")
            # 穷举m和n
            # for M in range(m, count_0 - 1, -1):
            #     for N in range(n, count_1 - 1, -1):
            #             dp[M][N] = max(dp[M][N], dp[M - count_0][N - count_1] + 1)
            for M in range(m, -1, -1):
                for N in range(n, -1, -1):
                    if M >= count_0 and N >= count_1:
                        dp[M][N] = max(dp[M][N], dp[M - count_0][N - count_1] + 1)               
        return dp[m][n]

    def findMaxForm_2(self, strs: List[str], m: int, n: int) -> int:
        """自顶向下的递归
        """
        if not strs: return 0
        memo = dict()
        def dfs(i, m, n):
            """
            i: 目前已经到决策树的第几层，初始值为0，表示第1层开始（也就是判断到第几个字符串了）
            m: 目前可用的0的数量，初始值为题目输入的m
            n: 目前可用的1的数量，初始值为题目输入的n
            """
            # 终止条件
            if i == len(strs):
                return 0
            if (i, m, n) in memo: return memo[(i,m, n)]
            res, count_0, count_1 = 0, strs[i].count("0"), strs[i].count("1")
            if m >= count_0 and n >= count_1:
                # 当前0和1的个数能够拼出字符串i
                res = 1 + dfs(i + 1, m - count_0, n - count_1)
            # 当前0和1的个数不能拼出字符串i
            res = max(res, dfs(i + 1, m, n))
            memo[(i, m, n)] = res
            return memo[(i, m, n)]
        return dfs(0, m, n)


if __name__ == "__main__":
    s = Solution()
    Array = ["10", "0", "1"]
    m = 1
    n = 1
    print(s.findMaxForm_2(Array, m, n))