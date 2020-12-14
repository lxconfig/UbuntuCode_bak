

"""
    给定一个二维数组，其中1代表岛屿，0代表海洋，问二维数组中有多少岛屿
"""


def numIslands(grid):
    if not grid:
        return 0
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                DFS(grid, i, j)
                count += 1
    return count


def DFS(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
        return
    
    grid[i][j] = "#"
    DFS(grid, i+1, j)  # 下
    DFS(grid, i-1, j)  # 上
    DFS(grid, i, j+1)  # 右
    DFS(grid, i, j-1)  # 左


def friends(grid):
    circle = 0
    n = len(grid)
    for i in range(n):
        if grid[i][i] != 1:
            continue
        friend = [i]
        while friend:
            f = friend.pop()
            if grid[f][f] == 0:
                continue
            grid[f][f] = 0
            for j in range(n):
                if grid[f][j] == 1 and grid[j][j] == 1:
                    friend.append(j)
        circle += 1
    return circle



if __name__ == "__main__":
    grid = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print(numIslands(grid))
    # print(friends(grid))
