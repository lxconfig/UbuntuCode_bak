# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def smallestFromLeaf_1(self, root: TreeNode) -> str:
        if not root: return ""
        dic, char = {}, "abcdefghijklmnopqrstuvwxyz"
        for i in range(26):
            dic[str(i)] = char[i]
        res, path = [], []
        def dfs(node):
            if not node: return 
            path.append(dic[str(node.val)])
            # 终止条件
            if not node.left and not node.right:
                res.append("".join(path[:]))
            dfs(node.left)
            dfs(node.right)
            path.pop()
        dfs(root)
        res = [x[::-1] for x in res]
        min_str = sorted(res)[0]
        return min_str


    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.res = "~"
        def dfs(node, path):
            if not node: return
            path.append(chr(node.val + ord("a")))
            if not node.left and not node.right:
                self.res = min(self.res, "".join(path[::-1]))
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root, [])
        return self.res