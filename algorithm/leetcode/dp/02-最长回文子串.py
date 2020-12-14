

"""
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """动态规划
        对于一个子串，如果它是回文串，并且长度大于2，那么去掉首尾两个字母后，剩下的部分肯定也是回文串
        记i，j分别表示字符串的下标，dp(i, j)表示字符串s中第i个字母到第j个字母组成的子串，那么：
                        True     如果子串si...sj是回文串
            dp(i, j) =   
                        False    其他情况
        其他情况包含：
            1. s[i, j]本身就不是回文串
            2. i > j，不存在这个子串
        则状态方程为：
            dp(i, j) = dp(i+1, j-1) and (Si == Sj)   len(S) > 2
        下面考虑特殊情况：
        当字符串s的长度=1时，显然是回文串
        当字符串s的长度=2时，只需要判断这两个字母是否相等即可
        所以，状态方程表示为：
            dp(i, j) = dp(i+1, j-1) and (Si == Sj)   len(S) > 2
            dp(i, i) = True                          len(S) == 1
            dp(i, i+1) = (Si == Si+1)                len(S) == 2
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        maxLen, begin = 1, 0
        # 一列一列的填值
        for j in range(1, n):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        # 表示字符串的长度为1或2，并且前提是s[i]==s[j]，所以该字符串肯定是回文串
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and (j - i + 1) > maxLen:
                    maxLen = j - i + 1
                    begin = i
        
        return s[begin: begin + maxLen]

    def longestPalindrome_1(self, s: str) -> str:
        if not s: return ""
        size, res = len(s), ""
        def helper(s, left, right):
            # 考虑越界问题
            while left >= 0 and right < size and s[left] == s[right]:
                # 当字符i两边的字符相等时，才继续扩散
                left -= 1
                right += 1
            # 不相等时，说明上一个位置的字符串就是当前最长的回文子串
            return s[left + 1: right]
        for i in range(size):
            s1 = helper(s, i, i)        # 找到以s[i]为中心的回文串
            s2 = helper(s, i, i + 1)    # 找到以s[i],s[i+1]为中心的回文串
            # 取长度最长的回文子串
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res

    def longestPalindrome_2(self, s: str) -> str:
        if not s: return ""
        size, max_len, start = len(s), 1, 0
        dp = [[False for _ in range(size)] for _ in range(size)]
        # base case
        for i in range(size):
            dp[i][i] = True
        
        for j in range(1, size):
            for i in range(0, j):
                # 需要分别讨论True和False的情况
                # 比如 cbbd，当i=1，j=2时，dp[1][2] = dp[2][1] and s[1] == s[2]
                # 由于dp[2][1]只被初始化为False，所以上面的dp[1][2] = False
                # 可是实际上dp[2][1]应该为True，因为bb显然是回文串 
                if s[i] == s[j]:
                    # 子串的范围是 j - 1 -(i + 1) + 1 < 2
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                # 直接在循环中处理
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start: start + max_len]


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome_2("cbbd"))