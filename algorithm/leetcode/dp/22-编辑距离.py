

"""
    给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
    你可以对一个单词进行如下三种操作：
        插入一个字符
        删除一个字符
        替换一个字符
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """自底向上
        """
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range (n+1)] for _ in range(m+1)]

        # base case
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1)
        # print(dp)
        return dp[m][n]
    
    def minDistance_1(self, word1: str, word2: str) -> int:
        """自顶向下的递归
        需要增加备忘录才不会超时
        """
        m, n = len(word1), len(word2)
        memo = dict()
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if i == -1: return j + 1
            if j == -1: return i + 1
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i-1, j-1)
            else:
                memo[(i, j)] = min(dp(i, j-1)+1, dp(i-1, j)+1, dp(i-1, j-1)+1)
            return memo[(i, j)]
        return dp(m-1, n-1)



if __name__ == "__main__":
    s = Solution()
    word1 = "horse"
    word2 = "ros"
    print(s.minDistance_1(word1, word2))