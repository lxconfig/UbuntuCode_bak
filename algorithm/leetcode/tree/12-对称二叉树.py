

"""
    给定一个二叉树，检查它是否是镜像对称的。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """递归法
        """
        if not root: return True

        def compare(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            if root1.val == root2.val:
                if compare(root1.left, root2.right) and compare(root1.right, root2.left):
                    return True
            return False
        return compare(root.left, root.right)
    
    def isSymmetric_1(self, root: TreeNode) -> bool:
        """遍历法
            先遍历一次原树，再遍历一次对称树
        """
        if not root: return True
        ret1 = self.PreOrder(root)
        root = self.Mirror(root)
        ret2 = self.PreOrder(root)
        return ret1 == ret2

    def PreOrder(self, root):
        if not root: return []
        stack, ret = [root], []
        while stack:
            node = stack.pop()
            if not node:
                ret.append(-999)
                return 
            stack.append(root.right)
            stack.append(root.left)
        return ret
        
    def Mirror(self, root):
        if not root: return None
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
