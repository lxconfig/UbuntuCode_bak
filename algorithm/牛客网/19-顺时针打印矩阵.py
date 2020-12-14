
"""
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 
    1  2  3  4 
    5  6  7  8 
    9  10 11 12 
    13 14 15 16 
    则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

    主要是边界的处理，如：输出完4，应该往下输出8
    还有判断已经输出过了

    运行时间：23ms
    占用内存：5736k
"""
import pysnooper

class Solution:
    # matrix类型为二维列表，需要返回列表
    # @pysnooper.snoop(output="./log.log", overwrite=True)
    def printMatrix(self, matrix):
        # write code here
        if not matrix and not matrix[0]:
            return None
        row, column = 0, 0
        row_border, column_border = len(matrix)-1, len(matrix[0])-1
        ret = []
        while row <= row_border and column <= column_border:
            # 向右
            for i in range(column, column_border+1):
                ret.append(matrix[column][i])
            # 向下
            for i in range(row+1, row_border+1):
                ret.append(matrix[i][column_border])
            # 向左
            if row != row_border:  # 当只有一行的时候，不需要向左
                for i in range(column_border-1, column-1, -1):
                    ret.append(matrix[row_border][i])
            # 向上   # 当只有一列的时候，不需要向上
            if column != column_border:
                for i in range(row_border-1, row, -1):
                    ret.append(matrix[i][column])
            row += 1
            row_border -= 1
            column += 1
            column_border -= 1
        return ret

    # def printMatrixs(self, matrix):
    #     row, col = 0, 0
    #     row_b, col_b = len(matrix)-1, len(matrix[0])-1
    #     ret = []
    #     while row <= row_b and col <= col_b:
    #         # 向右→
    #         for i in range(col, col_b+1):
    #             ret.append(matrix[row][i])
    #         # 向下↓
    #         for i in range(row+1, row_b+1):
    #             ret.append(matrix[i][col_b])
    #         # 向左←
    #         if row != row_b:
    #             for i in range(col_b-1, col-1, -1):
    #                 ret.append(matrix[row_b][i])
    #         # 向上↑
    #         if col != col_b:
    #             for i in range(row_b-1, row, -1):
    #                 ret.append(matrix[i][col])
    #         row += 1
    #         col += 1
    #         row_b -= 1
    #         col_b -= 1
    #     return ret


if __name__ == "__main__":
    solution = Solution()
    # matrix = [
    #     [1,2,3,4],
    #     [5,6,7,8],
    #     [9,10,11,12],
    #     [13,14,15,16],
    # ]
    # matrix = [
    #     [1],
    #     [2],
    #     [3],
    #     [4],
    #     [5]
    # ]
    matrix = [
        [1,2,3,4,5]
    ]
    print(solution.printMatrix(matrix))