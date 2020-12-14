
"""
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0: return [[]]
        res = []
        # 生成棋盘
        border = [["." for _ in range(n)] for _ in range(n)]
        self.backtracking(border, 0, res)
        return res

    def backtracking(self, border, row, res):
        """
        border: 代表棋盘
        row: 代表棋盘的某一行，初始值为0，表示从第1行开始放置皇后Q
        res: 结果集
        """
        n = len(border)
        # 终止条件
        # [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        if row == n:
            tmp_list = []
            for item in border:
                tmp_str = "".join(item)
                tmp_list.append(tmp_str)
            res.append(tmp_list)
            # return
        # 考虑选择
        # 考虑在第row行的每一列放置，找到一个合法的位置col
        for col in range(n):
            if not self.isValid(border, row, col):
                # 位置不合法，即和其他皇后Q冲突
                continue
            # 合法，做选择，放置皇后Q
            border[row][col] = "Q"
            # 进入下一层
            self.backtracking(border, row + 1, res)
            # 回溯，撤销选择
            border[row][col] = "."


    def isValid(self, border, row, col):
        """判断某个位置放置皇后Q是否合法
        border: 初始棋盘
        row: 代表某一行
        col: 代表某一列
        """
        # 检查其他行的第col列是否会冲突
        n = len(border)
        for other_row in range(n):
            if border[other_row][col] == "Q":
                return False
        
        # 判断右上是否冲突
        right_up_row, other_col = row - 1, col + 1
        while right_up_row >= 0 and other_col < n:
            if border[right_up_row][other_col] == "Q":
                return False
            right_up_row, other_col = right_up_row - 1, other_col + 1
        
        # 判断左上是否冲突
        left_up_row, other_col = row - 1, col - 1
        while left_up_row >= 0 and other_col >= 0:
            if border[left_up_row][other_col] == "Q":
                return False
            left_up_row, other_col = left_up_row - 1, other_col - 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))