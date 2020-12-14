
"""
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # if not root: return []
        # queue, res = [(0, root)], []
        # while queue:
        #     level, node = queue.pop(0)
        #     if len(res) == level: res.append([])
        #     if not res[level]:
        #         res[level].append(node.val)
        #     if node.right:
        #         queue.append((level + 1, node.right))
        #     if node.left:
        #         queue.append((level + 1, node.left))
        # return [i[0] for i in res]
        # 依据BFS的思想，每次遇到当前层最后一个元素才append
        if not root: return []
        queue, res = [root], []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == size - 1:
                    res.append(node.val)
        return res