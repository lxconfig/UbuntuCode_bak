

"""
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins_1(self, root: TreeNode, x: int, y: int) -> bool:
        # 先求节点x，y的深度，在判断它们的父节点是否不同
        # 但是这两步不好分开做，因为求深度的过程中就遍历了树 
        # 可以找到节点的父节点
        if not root: return False
        def GetDepth(root: TreeNode, target: int):
            queue, depth = [], 0
            queue.append([None, root])
            while queue:
                size = len(queue)
                for _ in range(size):
                    pair = queue.pop(0)
                    node = pair[1]
                    if node.val == target:
                        return (pair[0], depth)
                    if node.left:
                        queue.append([node, node.left])
                    if node.right:
                        queue.append([node, node.right])
                depth += 1
            # return depth
        x_pair = GetDepth(root, x)
        y_pair = GetDepth(root, y)
        return x_pair[1] == y_pair[1] and x_pair[0] != y_pair[0]

    def isCousins_2(self, root: TreeNode, x: int, y: int) -> bool:
        if not root: return False
        # 用两个字典维护深度和父节点
        depth, parent = {}, {}
        def dfs(node, par = None):
            if node:
                depth[node.val] = 1 + depth[par] if par else 0
                parent[node.val] = par
                dfs(node.left, node.val)
                dfs(node.right, node.val)
        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]