

"""
    给定一个二叉树，判断其是否是一个有效的二叉搜索树
"""
import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """递归法
        先定义出最大值和最小值
        若某个节点的值比最小值还要小或者比最大值还要大，则这颗子树肯定不是BST
        注：
            在对左子树进行判断时，最小值不变，最大值应该变为该左子树的根节点的值
            在对右子树进行判断时，最大值不变，最小值应该变为该右子树的根节点的值
        """
        return self.isBST(root, -sys.maxsize, sys.maxsize)
    
    def isBST(self, root, minValue, maxValue):
        if not root: return True
        if root.val < minValue or root.val > maxValue:
            return False
        
        return self.isBST(root.left, minValue, root.val) and self.isBST(root.right, root.val, maxValue)
    


    def isValidBST_1(self, root: TreeNode) -> bool:
        """中序遍历法
        由于二叉搜索树的中序遍历是一个升序数组，所以可以先定义出一个最小值num
        若某个节点的值比之前节点的值要小，说明肯定不是BST，可以直接返回False

        *** 要和前一个值进行比较，可以先记录下前一个值，如果正常，则用当前值替换前一个值 ***
        """
        # white, gray, num = 0, 1, float("-inf")
        # stack = [(white, root)]
        # while stack:
        #     color, node = stack.pop()
        #     if not node: continue
        #     if color == white:
        #         stack.append((white, node.right))
        #         stack.append((gray, node))
        #         stack.append((white, node.left))
        #     else:
        #         if node.val <= num:
        #             return False
        #         num = node.val
        # return True
        if not root: return True
        stack, node, num = [], root, float("-inf")
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.val <= num:
                    return False
                num = node.val
                node = node.right
        return True
        