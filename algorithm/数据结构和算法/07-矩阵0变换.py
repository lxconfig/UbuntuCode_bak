

def main():
    """
        将二维矩阵中，0所在行和列全部替换成0
        
        可以先找两个辅助列表，分别记录0对应的行和列
        之后再根据辅助列表，把原矩阵变换
    """
    matrix = [
        [1,1,1,0,1,1],
        [0,1,1,1,1,1],
        [1,0,1,1,1,1],
        [1,1,1,1,1,1]
    ]
    row = len(matrix)    # 行数
    column = len(matrix[0])  # 列数
    m, n = [None] * row, [None] * column

    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 0:
                m[i] = 1
                n[j] = 1

    for i in range(row):
        for j in range(column):
            if m[i] == 1 or n[j] == 1:
                matrix[i][j] = 0
    
    for i in range(row):
        print(matrix[i])
    


if __name__ == "__main__":
    main()