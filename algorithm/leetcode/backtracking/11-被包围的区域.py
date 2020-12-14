
"""
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        size_row, size_col = len(board), len(board[0])
        def dfs(row, col):
            # if not 0 <= row < size_row or not 0 <= col < size_col or board[row][col] != 'O':
            #     return
            if 0 <= row < size_row and 0 <= col < size_col and board[row][col] == 'O':
                board[row][col] = "A"
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        # 从边界开始遍历,注意：board并不一定是矩阵，所以边界需要画图看看
        # 上下边界
        for i in range(size_col - 1):
            dfs(0, i)             # 上边界
            dfs(size_row - 1, i)  # 下边界
        
        # 左右边界
        for j in range(size_row):
            dfs(j, 0)             # 左边界
            dfs(j, size_col - 1)  # 右边界

        # 边界上的"O"都被改为"A",其他位置的都还是"O"
        # 那么就可以继续遍历，把遇到的"A"->"O","O" -> "X"
        for i in range(size_row):
            for j in range(size_col):
                if board[i][j] == "X": continue
                elif board[i][j] == "A":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"