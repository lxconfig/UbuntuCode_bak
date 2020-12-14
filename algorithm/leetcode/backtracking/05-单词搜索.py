

"""
"""


from typing import List


class Solution:
    def __init__(self):
        self.derections = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns= len(board), len(board[0])
        if rows == 0: return False
        used = [[False for _ in range(columns)] for _ in range(rows)]

        # 遍历每一行每一列的字符
        for row in range(rows):
            for col in range(columns):
                if board[row][col] == word[0]:
                    # 先标记为used
                    used[row][col] = True
                    if self.backtracking(board, row, col, word[1:], used):
                        return True
                    else:
                        # 回溯
                        used[row][col] = False
        return False

    def backtracking(self, board, row, col, word, used):
        """
        board: 初始二维网格，即搜索空间
        row: 从第一行开始搜索，初始值为0
        used: 表示某个字符是否被使用过
        """
        # 终止条件
        if not word: return True
        rows, columns = len(board), len(board[0])
        for direction in self.derections:
            cur_row = row + direction[0]
            cur_col = col + direction[1]
            if cur_row >= 0 and cur_row < rows and cur_col >= 0 and cur_col < columns and board[cur_row][cur_col] == word[0]:
                # 位置坐标都合法，并且等于要找的字符串
                if used[cur_row][cur_col]:
                    # 使用过该字符
                    continue
                used[cur_row][cur_col] = True
                if self.backtracking(board, cur_row, cur_col, word[1:], used):
                    return True
                else:
                    used[cur_row][cur_col] = False
        return False


if __name__ == "__main__":
    s = Solution()
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word = "SEE"
    print(s.exist(board, word))