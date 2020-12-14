



class Solution:
    def MaxA(self, N: int) -> int:
        if not N: return 0
        def dp(i, j, c):
            # i表示按键次数，j表示屏幕上字母A的数量，c表示缓冲区字母A的数量
            if i <= 0: return j
            return max(
                dp(i-1, j+1, c),
                dp(i-1, j+c, c),
                dp(i-2, j, j)
            )
        return dp(N, 0, 0)

    def MaxA_1(self, N: int) -> int:
        """添加备忘录
        """
        if not N: return 0
        memo = dict()
        def dp(i, j, c):
            # i表示按键次数，j表示屏幕上字母A的数量，c表示缓冲区字母A的数量
            if i <= 0: return j
            if (i, j, c) in memo: return memo[(i, j, c)]
            memo[(i, j, c)] =  max(
                dp(i-1, j+1, c),
                dp(i-1, j+c, c),
                dp(i-2, j, j)
            )
            return memo[(i, j, c)]
        return dp(N, 0, 0)
    
    def MaxA_2(self, N: int) -> int:
        if not N: return 0
        dp = [0 for _ in range(N+1)]
        for i in range(1, N+1):
            dp[i] = dp[i-1] + 1   # 仅按A键
            for j in range(2, i):
                dp[i] = max(dp[i], dp[j-2] * (i - j + 1))
        print(dp)
        return dp[N]



if __name__ == "__main__":
    s = Solution()
    print(s.MaxA_2(7))