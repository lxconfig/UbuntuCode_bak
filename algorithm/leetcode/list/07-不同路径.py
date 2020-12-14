

"""
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）
    总共有多少条不同的路径？
"""
import pysnooper


class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        # m表示列，n表示行
        if m == 0 or n == 0 or not m or not n:
            return 0
        return self.DFS(m, n)

    def DFS(self, m, n):
        if m == 1 and n == 1:
            return 1
        route = 0
        if m > 0:
            route += self.DFS(m - 1, n)
        if n > 0:
            route += self.DFS(m, n - 1)
        return route
        
    def uniquePaths_2(self, m: int, n: int) -> int:
        """动态规划
        定义i，j表示网格中的位置，dp[i][j]表示起点到(i,j)的路径数
        显然：
            dp[0][0] = 1
            dp[i][0] = 1
            dp[0][j] = 1
        对于其他位置：
            由于只能向下或向右移动，则： dp[i][j] = dp[i-1][j] + dp[i][j-1]
        总结：
            dp[i][j] = dp[i-1][j] + dp[i][j-1]    i != 0 and j != 0
            dp[i][j] =  1                         i == 0 or j == 0
        """
        if m == 0 or n == 0 or not m or not n:
            return 0
        
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                # elif j == 0:
                #     dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]
    
    def uniquePaths_3(self, m: int, n: int) -> int:
        """动态规划-优化版
        """
        dp = [[1] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths_3(7,3))