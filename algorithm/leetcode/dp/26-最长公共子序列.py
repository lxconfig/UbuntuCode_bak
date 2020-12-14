


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]
    

    def longestCommonSubsequence_1(self, text1: str, text2: str) -> int:
        memo = dict()
        def dp(i, j):
            if i == -1 or j == -1: return 0
            if (i, j) in memo: return memo[(i, j)]
            elif text1[i] == text2[j]:
                memo[(i, j)] = dp(i - 1, j - 1) + 1
            else:
                memo[(i, j)] = max(dp(i - 1, j), dp(i, j - 1))
            return memo[(i, j)]
        return dp(len(text1) - 1, len(text2) - 1)


if __name__ == "__main__":
    s = Solution()
    text1 = "abcde"
    text2 = "ace" 
    print(s.longestCommonSubsequence(text1, text2))