
"""
    给定两个二叉树，编写一个函数来检验它们是否相同。
    如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """递归法
        """
        if not p and not q: return True
        if p == None and q != None: return False
        if p != None and q == None: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def isSameTree_1(self, p: TreeNode, q: TreeNode) -> bool:
        """遍历法
            颜色标记法会超时
        """    
        def InOrder(root):
            if not root: return [None]
            else:
                return [root.val] + InOrder(root.left) + InOrder(root.right)
        return InOrder(p) == InOrder(q)