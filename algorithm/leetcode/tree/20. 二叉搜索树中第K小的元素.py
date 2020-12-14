
"""
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 中序遍历
        white, gray, res = 0, 1, []
        stack = [(root, white)]
        while stack:
            node, color = stack.pop()
            if not node: continue
            if color == white:
                stack.append((node.right, white))
                stack.append((node, gray))
                stack.append((node.left, white))
            else:
                res.append(node.val)
        return res[k - 1]

    def kthSmallest_1(self, root: TreeNode, k: int) -> int:
        """遍历过程中，记录节点数，直到等于k，就可以输出
        """
        # 中序遍历
        def inOrder(node):
            if not node: return 
            inOrder(node.left)
            self.nums += 1
            if self.nums == k:
                self.res = node.val
                return 
            inOrder(node.right)
        # if not root: return 0
        self.nums, self.res = 0, 0
        inOrder(root)
        return self.res