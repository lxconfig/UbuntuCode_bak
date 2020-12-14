

"""
    请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        """
            用两个栈来保存二叉树中奇数层和偶数层的节点
        """
        if not pRoot:
            return None
        odd, even, ret = [], [pRoot], []

        while odd or even:
            tmp, tmps = [], []
            while even:
                node = even.pop()
                tmp.append(node)
                if node.left:
                    odd.append(node.left)
                if node.right:
                    odd.append(node.right)
            if tmp:
                ret.append(tmp)
            while odd:
                node = odd.pop()
                tmps.append(node)
                if node.right:
                    even.append(node.right)
                if node.left:
                    even.append(node.left)
            if tmps:
                ret.append(tmps)
        return ret