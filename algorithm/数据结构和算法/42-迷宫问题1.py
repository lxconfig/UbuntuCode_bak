
"""
    输入一个二维矩阵，并给定起始坐标及终点坐标，在矩阵中，1代表是墙，不能通过，0代表是路径，可以通过。
    问能否找到一条路径通向终点坐标，能则返回True，否则返回False
    0 0 1 0 0
    1 0 0 1 0
    0 1 1 0 0
    1 0 0 1 0
    0 0 1 0 1
    
    将0看作是图中的顶点
"""

def Maze(matrix, start, end):
    visited = [[False] * len(matrix) for _ in range(len(matrix))]
    return MazeHelper(matrix, start, end, visited)

def MazeHelper(matrix, start, end, visited):
    """递归写法
    """
    # base情况
    if start[0] == end[0] and start[1] == end[1]:
        # 起点和终点相同
        return True
    if visited[start[0]][start[1]] == True:
        # 起点已经访问过
        return False
    if matrix[start[0]][start[1]] == 1:
        # 起点位置走不通
        return False
    
    visited[start[0]][start[1]] = True

    # 找到起点位置的四个邻居(2-4个)
    if start[0] - 1 >= 0:
        # 向上走
        up = (start[0] - 1, start[1])
        # return MazeHelper(matrix, up, end, visited)  # 这样写的话，当A往下走了一个点到B，B又可以往上走，走回之前的点A，由于A被访问过，所以肯定会返回False
        if MazeHelper(matrix, up, end, visited):
            return True
    
    if start[0] + 1 <= len(matrix) - 1:
        # 向下走
        down = (start[0] + 1, start[1])
        if MazeHelper(matrix, down, end, visited):
            return True
    
    if start[1] - 1 >= 0:
        # 向左走
        left = (start[0], start[1] - 1)
        if MazeHelper(matrix, left, end, visited):
            return True
    
    if start[1] + 1 <= len(matrix) - 1:
        # 向右走
        right = (start[0], start[1] + 1)
        if MazeHelper(matrix, right, end, visited):
            return True
    
    return False


def MazeIterative(matrix, start, end):
    """循环写法
    """
    visited = [[False] * len(matrix) for _ in range(len(matrix))]
    stack = [start]
    visited[start[0]][start[1]] = True
    destination = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 代表上下左右四个方向
    while stack:
        vertex = stack.pop()
        if vertex[0] == end[0] and vertex[1] == end[1]:
            return True
        
        # 找到邻居节点
        for dest in destination:
            x = vertex[0] + dest[0]
            y = vertex[1] + dest[1]

            # 判断边界
            if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix)):
                # 说明没有某个方向的邻居,进行下次循环
                continue
            if matrix[x][y] == 1:
                continue
            if visited[x][y]:
                continue
            visited[x][y] = True
            stack.append((x, y))
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
    print(MazeIterative(matrix, start, end))