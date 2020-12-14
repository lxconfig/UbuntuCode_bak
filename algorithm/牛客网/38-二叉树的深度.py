
"""
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # 递归
        # 运行时间：22ms  占用内存：5860k
        return self.__TreeDepth(pRoot)

    def __TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        
        return 1 + max(self.__TreeDepth(pRoot.left), self.__TreeDepth(pRoot.right))


if __name__ == "__main__":
    pass