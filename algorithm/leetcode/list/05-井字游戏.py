

"""
    设计一个算法，判断玩家是否赢了井字游戏。输入是一个 N x N 的数组棋盘，由字符" "，"X"和"O"组成，其中字符" "代表一个空位。
    如果游戏存在获胜者，就返回该游戏的获胜者使用的字符（"X"或"O"）；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。
"""


class Solution:
    def tictactoe(self, board: list) -> str:
        N = len(board)
        pending = False
        row_x, col_x, row_o, col_o = [0] * N, [0] * N, [0] * N, [0] * N
        diagonal_x, diagonal_o = [0] * 2, [0] * 2   # 对角线只有两条
        for i in range(N):
            for j in range(N):
                if board[i][j] == "X":
                    row_x[i] += 1
                    col_x[j] += 1
                    if i == j:
                        diagonal_x[0] += 1
                    if i + j == N - 1:
                        diagonal_x[1] += 1
                elif board[i][j] == "O":
                    row_o[i] += 1
                    col_o[j] += 1
                    if i == j:
                        diagonal_o[0] += 1
                    if i + j == N - 1:
                        diagonal_o[1] += 1
                elif board[i][j] == " ":
                    pending = True
        print(row_x, col_x, diagonal_x)
        print(row_o, col_o, diagonal_o)
        print(N)
        if N in row_o or N in col_o or N in diagonal_o:
            return "O"
        elif N in row_x or N in col_x or N in diagonal_x:
            return "X"
        return "Pending" if pending else "Draw"


if __name__ == "__main__":
    s = Solution()
    board = ["O X"," XO","X O"]
    print(s.tictactoe(board))