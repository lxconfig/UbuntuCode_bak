

"""
    地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 
    例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""


class Solution:
    def movingCount(self, threshold, rows, cols):
        # 运行时间：31ms  占用内存：5856k
        if not rows or not cols or threshold < 0:
            return 0
        if threshold == 0:
            return 1
        # matrix = [[i+j for i in range(cols)] for j in range(rows)]

        visited = [[False] * cols for _ in range(rows)]
        start = (0, 0)
        self.DFS(threshold, rows, cols, start, visited)
        count = 0
        for i in visited:
            count += i.count(True)
        return count
        # return visited
        

    def DFS(self, threshold, rows, cols, start, visited):
        if start[0] < 0 or start[1] < 0 or start[0] >= rows or start[1] >= cols:
            # 越界
            return False
        if visited[start[0]][start[1]] == True:
            # 访问过
            return False
        # if matrix[start[0]][start[1]] > threshold:
        #     return False

        # 计算两个坐标的和是否大于threshold
        tmp = list(str(start[0]))
        tmp.extend(list(str(start[1])))
        num = 0
        for i in tmp:
            num += int(i)
        if num > threshold:
            return False
        
        visited[start[0]][start[1]] = True

        # 移动到上下左右节点继续判断
        if start[0] - 1 >= 0:
            # 上
            up = (start[0] - 1, start[1])
            if self.DFS(threshold, rows, cols, up, visited):
                return True
        if start[0] + 1 <= rows - 1:
            # 下
            down = (start[0] + 1, start[1])
            if self.DFS(threshold, rows, cols, down, visited):
                return True
        if start[1] - 1 >= 0:
            # 左
            left = (start[0], start[1] - 1)
            if self.DFS(threshold, rows, cols, left, visited):
                return True
        if start[1] + 1 <= cols - 1:
            # 右
            right = (start[0], start[1] + 1)
            if self.DFS(threshold, rows, cols, right, visited):
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.movingCount(10, 1, 100))