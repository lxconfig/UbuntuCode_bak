
"""
    给定一个 N 叉树，找到其最大深度。
    最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
"""



# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        """BFS
        """
        if not root: return 0
        queue, depth = [], 1
        queue.append(root)
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if not node.children and not queue:
                    return depth
                for child in node.children:
                    queue.append(child)
            depth += 1
        return depth

    def maxDepth_1(self, root: 'Node') -> int:
        """DFS
        """
        if not root: return 0
        stack, max_depth ,depth = [], float("-inf") , 1
        stack.append(root)
        while stack:
            size = len(stack)
            for _ in range(size):
                node = stack.pop(0)
                if not node.children:
                    max_depth = max(max_depth, depth)
                for child in node.children:
                    stack.append(child)
            depth += 1
        return max_depth