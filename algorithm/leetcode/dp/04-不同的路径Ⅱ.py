

"""
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        if not obstacleGrid: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        # 初始化
        for i in range(m):
            if obstacleGrid[i][0] == 1: break
            else:
                dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1: break
            else:
                dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    # 考虑的是i,j位置如何走到，要么是前一个位置向下走到的，
                    # 要么是前一个位置向右走到的
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]
    

if __name__ == "__main__":
    s = Solution()
    obstacleGrid = [
        [0]
    ]
    print(s.uniquePathsWithObstacles(obstacleGrid))