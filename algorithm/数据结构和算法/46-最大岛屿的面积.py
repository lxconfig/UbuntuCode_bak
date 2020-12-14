

"""
    求最大的岛屿面积
"""

def MaxAreaOfIsland(grid):
    MaxArea = 0

    def DFS(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + DFS(i+1, j) + DFS(i-1, j) + DFS(i, j+1) + DFS(i, j-1)
        return 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                MaxArea = max(MaxArea, DFS(i, j))
    return MaxArea


if __name__ == "__main__":
    grid = [
        [1, 1, 0],
        [0, 0, 1],
        [1, 1, 0]   
    ]
    print(MaxAreaOfIsland(grid))