


"""
    给定两个字符串，求其中的longest common substring最长公共子序列LCS(子序列不一定是连续的)
    例：s1 = GABRETC   s2 = AEBTUFD   LCS = AB
"""


def LongestCommonSubstring(s1, s2):
    """二维动态规划
    记i,j分别表示两种状态，i表示s1字符串的前i个，j表示s2字符串的前j个
    dp[i][j]表示s1的前i个字符与s2的前i个字符中LCS的长度
    则: 
        dp[0][j] = dp[i][0] = 0                  i = 0 or j = 0
                   dp[i-1][j-1] + 1              s1[i] == s2[j]     当s1[i] == s2[j]时，只需要考虑前面的字符串即可
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])   s1[i] != s2[j]     当两者不等时，要么考虑i前面的，要么考虑j前面的
    """
    if not s1 or not s2:
        return None
    
    m, n = len(s1) + 1, len(s2) + 1
    dp = [[0 for _ in range(m)] for _ in range(n)]
    # lcs = ""
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:    # 因为m和n是字符串长度+1，所以会越界，而且0的情况都在前面处理掉了，因此这里写i-1，j-1即可
                dp[i][j] = dp[i-1][j-1] + 1
                # lcs += s1[i-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m-1][n-1]


if __name__ == "__main__":
    s1 = "01101"
    s2 = "10011"
    print(LongestCommonSubstring(s1, s2))