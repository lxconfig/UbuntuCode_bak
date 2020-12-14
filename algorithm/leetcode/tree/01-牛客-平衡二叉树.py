
"""
    输入一棵二叉树，判断该二叉树是否是平衡二叉树。
    在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.DFS(pRoot) != -1
    
    def DFS(self, p):
        if not p:
            return 0
        left = self.DFS(p.left)
        if left == -1:
            return -1
        right = self.DFS(p.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1