
"""
    给定一个二叉树，在树的最后一行找到最左边的值
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        """BFS
        """
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            self.value = queue[0].val
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return self.value
    def findBottomLeftValue_1(self, root: TreeNode) -> int:
        """改进版BFS
        """
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val

    def findBottomLeftValue_2(self, root: TreeNode) -> int:
        """DFS
        """
        self.max_depth, depth, self.value = -1, 0, 0
        def dfs(node, depth):
            if not node: return 
            if depth > self.max_depth:
                self.max_depth = depth
                self.value = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, depth)
        return self.value