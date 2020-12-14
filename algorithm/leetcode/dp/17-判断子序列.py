


"""
    给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
    你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """双指针法
        """
        if not s and not t: return True
        size_s, size_t = len(s), len(t)
        i, j = 0, 0
        while i < size_s and j < size_t:
            if s[i] == t[j]:
                i, j = i + 1, j + 1
            else:
                j += 1
        return i == size_s
    
    def isSubsequence_1(self, s: str, t: str) -> bool:
        """动态规划
        """
        if not s and not t: return True
        size_s, size_t = len(s), len(t)
        dp = [[False] * (size_t+1) for _ in range (size_s+1)]
        for j in range(size_t):
            dp[0][j] = True
        for i in range(1, size_s+1):
            for j in range(1, size_t+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[size_s][size_t]


    def isSubsequence_2(self, s: str, t: str) -> bool:
        """自底向上的动态规划
        """
        m, n = len(s), len(t)
        dp = [[False for _ in range (n+1)] for _ in range(m+1)]

        # base case
        for j in range(n+1):
            dp[0][j] = True
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[m][n]

    def isSubsequence_3(self, s: str, t: str) -> bool:
        """自顶向下的递归
        """
        m, n = len(s), len(t)
        memo = dict()
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if i == -1: return True
            if j == -1: return False
            if s[i] == t[j]:
                memo[(i, j)] = dp(i-1, j-1)
            else:
                memo[(i, j)] =  dp(i, j-1)
            return memo[(i, j)]
        return dp(m-1, n-1)


if __name__ == "__main__":
    ss = Solution()
    s = "abc"
    t = "ahbgdc"
    print(ss.isSubsequence_3(s, t))