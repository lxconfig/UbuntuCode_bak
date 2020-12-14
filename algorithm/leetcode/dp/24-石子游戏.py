

from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """斜着遍历
        """
        size = len(piles)
        dp = [[[0, 0] for _ in range(size)] for _ in range(size)]
        # base case
        for i in range(size):
            dp[i][i][0] = piles[i]
            # dp[i][i][1] = 0
        
        for L in range(2, size+1):
            for i in range(size-L+1):
                j = L + i - 1
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]
        # print(dp)
        return bool(dp[0][size-1][0] - dp[0][size-1][1])

    def stoneGame_1(self, piles: List[int]) -> bool:
        """也可以对列从左往右遍历，对行从下往上遍历，来填dp表
        """
        size = len(piles)
        # [0, 0]分别表示先手和后手能获得的最多石子数
        dp = [[[0, 0] for _ in range(size)] for _ in range(size)]
        # base case
        for i in range(size):
            dp[i][i][0] = piles[i]
            # dp[i][i][1] = 0
        
        for j in range(1, size):
            for i in range(j-1, -1, -1):
                # 0表示先手，1表示后手
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]
        return bool(dp[0][size-1][0] - dp[0][size-1][1])


if __name__ == "__main__":
    s = Solution()
    print(s.stoneGame_1([3, 9, 1, 2]))