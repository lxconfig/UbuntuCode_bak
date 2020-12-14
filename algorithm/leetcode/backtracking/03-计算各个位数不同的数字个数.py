

"""
"""


from typing import List


class Solution:
    def __init__(self):
        self.res = 0
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        used, depth= [False for _ in range(10)], 0

        def dfs(depth, used):
            # nonlocal res   # 表明res是外部函数的变量
            # 终止条件,表示已经有n位数
            if depth == n:
                return 
            # 针对十位进行穷举
            for i in range(10):
                # if i == 0 and depth == 1:
                #     continue
                # if used[i]:
                #     continue
                # 剪枝的策略是：当位数只有2位，并且used[0]已经使用过时，就没有其他数字可选 
                # used[0]表示的就是数字0是否被选择，depth是从0开始的，所以depth=1表示的应该是两位数
                if used[0] and depth == 1:
                    continue
                if not used[i]:
                    used[i] = True
                    self.res += 1
                    dfs(depth + 1, used)
                    used[i] = False
        dfs(depth, used)
        return self.res

    def countNumbersWithUniqueDigits_1(self, n: int) -> int:
        """动态规划
        """
        if n == 0: return 1
        dp = [0 for _ in range(n + 1)]
        dp[0], dp[1] = 1, 9
        res = dp[0] + dp[1]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (10 - i + 1)
            res += dp[i]
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.countNumbersWithUniqueDigits_1(3))