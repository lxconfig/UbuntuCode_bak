# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        path = []
        def dfs(node, path):
            if not node: return 
            path.append(node.val)
            if not node.left and not node.right:
                self.res = max(self.res, abs(max(path) - min(path)))
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root, path)
        return self.res

    def maxAncestorDiff_1(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        def dfs(node, max_val, min_val):
            if not node: return 
            max_val = max(max_val, node.val)
            min_val = min(min_val, node.val)
            if not node.left and not node.right:
                self.res = max(self.res, abs(max_val - min_val))
            if node.left:
                dfs(node.left, max_val, min_val)
            if node.right:
                dfs(node.right, max_val, min_val)
        dfs(root, root.val, root.val)
        return self.res
