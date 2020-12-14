

"""
    给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """递归
        到某个节点时，判断其是否是叶子节点并且值是否等于sum
        若不是，则递归判断左右子树
        注：
            递归判断时，需要减去当前root的值
        """
        if not root: return False
        if not root.left and not root.right: return root.val == sum
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

    def hasPathSum_1(self, root: TreeNode, sum: int) -> bool:
        """迭代
        每次把之前节点的值加起来
        """
        if not root: return False
        stack = [(root.val, root)]
        while stack:
            value, node = stack.pop()
            if not node.left and not node.right and value == sum:
                return True
            if node.right:
                stack.append((value + node.right.val, node.right))
            if node.left:
                stack.append((value + node.left.val, node.left))
        return False
    

if __name__ == "__main__":
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(8)
    d = TreeNode(11)
    e = TreeNode(13)
    f = TreeNode(4)
    g = TreeNode(7)
    h = TreeNode(2)
    i = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    c.left = e
    c.right = f
    d.left = g
    d.right = h
    f.right = i
    s = Solution()
    print(s.hasPathSum(a, 22))