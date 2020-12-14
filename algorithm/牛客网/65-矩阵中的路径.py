

"""
    请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
    如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。

    例如：
        a b c e
        s f c s
        a d e e
    包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子

    思路:
        图论中的DFS
"""
# import pysnooper


class Solution:
    def __init__(self):
        self.index = 0
    
    def hasPath(self, matrix, rows, cols, path):
        # 运行时间：35ms  占用内存：5856k
        matrix = [list(matrix[cols*i: cols*i+cols]) for i in range(rows)]
        if not path:
            return False
        visited = [[False] * cols for _ in range(rows)]
        # @pysnooper.snoop()
        def helper(x, y):
            """DFS遍历
            """
            if x < 0 or x >= rows or y < 0 or y >= cols:
                # 起点的位置不合法
                return False
            if matrix[x][y] != path[self.index]:
                # 当前位置的值和path路径中的值不等
                return False
            if visited[x][y]:
                # 起点已经访问过
                return False
            if self.index == len(path) - 1:
                # 已经匹配到最后一个字符
                return True

            # 记录x，y已经访问过
            visited[x][y] = True
            self.index += 1
            # if helper(x-1, y) or helper(x+1, y) or helper(x, y-1) or helper(x, y+1):
            #     return True

            if x - 1 >= 0:
                up = x - 1
                if helper(up , y):
                    return True
            if x + 1 <= rows - 1:
                down = x + 1
                if helper(down, y):
                    return True
            if y - 1 >= 0:
                left = y - 1
                if helper(x, left):
                    return True
            if y + 1 <= cols - 1:
                right = y + 1
                if helper(x, right):
                    return True

            # 走到这说明之前都没有返回，也就是这条路是走不通的，重置状态和index
            visited[x][y] = False
            self.index -= 1
            return False

        for i in range(rows):
            for j in range(cols):
                if helper(i, j):
                    return True
        
        return False


if __name__ == "__main__":
    solution = Solution()
    matrix = 'abcesfcsadee'
    rows = 3
    cols = 4
    path = "abcb"
    print(solution.hasPath(matrix, rows, cols, path))