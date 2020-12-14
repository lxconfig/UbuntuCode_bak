

"""
    给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """递归法
        """
        if not root: return None

        def helper(root):
            if not root: return None
            if root.val == val:
                return root
            elif root.val > val:
                return helper(root.left)
            else:
                return helper(root.right)
        
        return helper(root)

    def searchBST_1(self, root: TreeNode, val: int) -> TreeNode:
        """迭代法
        """
        if not root: return None
        while root and root.val != val:
            if root.val < val:
                root = root.right
            else:
                root = root.left
        return root




if __name__ == "__main__":
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(7)
    d = TreeNode(1)
    e = TreeNode(3)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    s = Solution()
    print(s.searchBST(a, 2))