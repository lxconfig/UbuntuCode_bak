

"""
"""


class Solution:
    def minimumTotal(self, triangle: list) -> int:
        """自顶向下的动态规划
        """
        if not triangle: return 0
        # n表示层数
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            # i表示层数，j表示下标
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        
        return min(dp[n-1])
    
    def minimumTotal_1(self, triangle: list) -> int:
        """自底向上的动态规划
        """
        if not triangle: return 0   
        size = len(triangle)
        dp = [[0] * (size+1) for _ in range(size+1)]

        for i in range(size-1, -1, -1):
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]


    def minimumTotal_2(self, triangle: list) -> int:
        """自底向上的动态规划
        空间优化
        发现dp[i][j]只和下一层dp[i+1][j]或dp[i+1][j+1]有关联
        所以，可以去掉i这个维度
        """
        if not triangle: return 0
        size = len(triangle)
        dp = [0] * (size + 1)

        for i in range(size-1, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]


if __name__ == "__main__":
    s = Solution()
    triangle = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
    print(s.minimumTotal_1(triangle))
