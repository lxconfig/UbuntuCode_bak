

"""
    对迷宫问题1进行改进，起点在尝试某条路径时，只有碰到墙(即1)或超出边界才能停下来，问是否有能达到终点的路径

    思路：在遍历起点的邻居节点时，不是单独的if判断，而是要继续循环下去，直到碰到墙或边界
"""

def Maze(matrix, start, end):
    visited = [[False] * len(matrix) for _ in range(len(matrix))]
    return MazeHelper(matrix, start, end, visited)


def MazeHelper(matrix, start, end, visited):
    if start[0] == end[0] and start[1] == end[1]:
        return True
    
    if matrix[start[0]][start[1]] == 1:
        return False
    
    if visited[start[0]][start[1]]:
        return False
    
    visited[start[0]][start[1]] = True
    
    up = start[0] - 1
    down = start[0] + 1
    left = start[1] - 1
    right = start[1] + 1

    # 循环找邻居节点
    while up >= 0 and matrix[up][start[1]] == 0:
        # 向上
        up -= 1
    # 循环结束说明up位置不合适，或者碰到墙，就要退回到上一个位置
    before_up = (up + 1, start[1])
    if MazeHelper(matrix, before_up, end, visited):
        return True
    
    while down <= len(matrix) - 1 and matrix[down][start[1]] == 0:
        # 向下
        down += 1
    before_down = (down - 1, start[1])
    if MazeHelper(matrix, before_down, end, visited):
        return True
    
    while left >= 0 and matrix[start[0]][left] == 0:
        # 向左
        left -= 1
    before_left = (start[0], left + 1)
    if MazeHelper(matrix, before_left, end, visited):
        return True
    
    while right <= len(matrix) - 1 and matrix[start[0]][right] == 0:
        # 向右
        right += 1
    before_right = (start[0], right - 1)
    if MazeHelper(matrix, before_right, end, visited):
        return True

    return False


if __name__ == "__main__":
    matrix = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)

    print(Maze(matrix, start, end))