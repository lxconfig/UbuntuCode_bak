

"""
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        self.res, path = 0, ""
        
        def dfs(node, path):
            # print("刚进入：", id(path))
            if node:
                path += str(node.val)
                # print("添加元素后：", id(path))
                if not node.left and not node.right:
                    self.res += int(path)
                dfs(node.left, path)
                dfs(node.right, path)
        dfs(root, path)
        return self.res

    def sumNumbers_1(self, root: TreeNode) -> int:
        if not root: return 0
        res, path = [], []
        
        def dfs(node, path):
            if node:
                path.append(node.val)
                if not node.left and not node.right:
                    res.append(path[:])
                dfs(node.left, path)
                dfs(node.right, path)
                path.pop()
        dfs(root, path)
        return [str(i) + str(j) for i, j in res]   # 返回["12", "13"]


if __name__ == "__main__":
    s = Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c
    print(s.sumNumbers_1(a))