
"""
"""

from typing import List


class Solution:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        size_row, size_col, count = len(grid), len(grid[0]), 0
        used = [[False for _ in range(size_col)] for _ in range(size_row)]
        # 从第一行第一列开始遍历
        for i in range(size_row):
            for j in range(size_col):
                if not used[i][j] and grid[i][j] == "1":
                    used[i][j] = True
                    count += 1
                    self.dfs(grid, i, j, count, size_row, size_col, used)
        return count
        
    def dfs(self, grid, row, col, count, size_row, size_col, used):
        for direction in self.directions:
            cur_row, cur_col = row + direction[0], col + direction[1]
            if 0 <= cur_row < size_row and 0 <= cur_col < size_col and not used[cur_row][cur_col] and grid[cur_row][cur_col] == "1":
                used[cur_row][cur_col] = True
                count += 1
                self.dfs(grid, cur_row, cur_col, count, size_row, size_col, used)