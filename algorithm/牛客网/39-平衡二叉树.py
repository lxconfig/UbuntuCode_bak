

"""
    输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = True
    
    def IsBalanced_Solution(self, pRoot):
        # 暴力递归
        # 运行时间：34ms  占用内存：5840k
        if not pRoot:
            return True
        return abs(self.__TreeDepth(pRoot.left) - self.__TreeDepth(pRoot.right)) <= 1 and self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def __TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        return 1 + max(self.__TreeDepth(pRoot.left), self.__TreeDepth(pRoot.right))

    def IsBalanced_Solution2(self, pRoot):
        # 减少一些计算次数
        # 运行时间：35ms  占用内存：5752k
        if not pRoot:
            return True
        self.helper(pRoot)
        return self.res

    def helper(self, root):
        if not root:
            return 0
        if not self.res:
            return 1
        left = 1 + self.helper(root.left)
        right = 1 + self.helper(root.right)

        if abs(left - right) > 1:
            # 说明这个子树不是平衡的，也就不用继续计算下去
            self.res = False
        return max(left, right)