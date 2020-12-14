

"""
    给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
"""


class Solution:
    def minPathSum(self, grid: list) -> int:
        """动态规划-从左上角出发
        dp[i][j]表示为了到达(i,j)位置，需要的最小路径和是多少
        即：为了到达(i,j)，只能是从其上面位置往下走，或者左边位置往右走
        如：dp[1][1] = min(dp[0][1], dp[1][0]) + grid[1][1]
        也就是以(i,j)位置为中心，检查上面走下来，或者左边走过来谁更小

            dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
        特殊情况：
            第一行和第一列由于只有一种可能的走法，所以不用判断最小值
        """
        if not grid: return 0
        # 行，列
        row, col = len(grid), len(grid[0])
        dp = [[9999] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
        # print(dp)
        return dp[row-1][col-1]




if __name__ == "__main__":
    s = Solution()
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(s.minPathSum(grid))