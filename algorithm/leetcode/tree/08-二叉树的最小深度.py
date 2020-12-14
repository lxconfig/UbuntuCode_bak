

"""
    给定一个二叉树，找出其最小深度。
    二叉树的深度为根节点到最近叶子节点的最长路径上的节点数
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """递归法（自底向上）
        """
        if not root: return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        if leftDepth and rightDepth:
            # 左右子树深度均不为0
            return 1 + min(leftDepth, rightDepth)
        # 有任意子树深度为0，则返回另一个子树的深度+1
        elif leftDepth == 0 and rightDepth != 0:
            return 1 + rightDepth
        elif rightDepth == 0 and leftDepth != 0:
            return 1 + leftDepth
        else:
            # 左右子树深度均为0，则返回1(根节点深度)
            return 1
    
    def minDepth_1(self, root: TreeNode) -> int:
        """BFS
        由于BFS是一层一层往下遍历，所以当到达叶子节点可以直接返回深度
        BFS用队列实现，先左子树再右子树
        """
        if not root: return 0
        queue = [(1, root)]
        while queue:
            depth, node = queue.pop(0)
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((depth+1, node.left))
            if node.right:
                queue.append((depth+1, node.right))
    
    def minDepth_2(self, root: TreeNode) -> int:
        """DFS
        由于DFS是一条路走到黑的遍历，所以先到达的叶子节点不一定就是最小深度
        则记录下每次遇到叶子节点时，和上一个叶子节点的深度比较，取较小的深度返回
        DFS用栈实现，先右子树再左子树
        """
        if not root: return 0
        stack = [(1, root)]
        min_depth = float("inf")
        while stack:
            depth, node = stack.pop()
            if not node.left and not node.right:
                min_depth = min(min_depth, depth)
            if node.right:
                stack.append((depth+1, node.right))
            if node.left:
                stack.append((depth+1, node.left))
        return min_depth


if __name__ == "__main__":
    s = Solution()
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(8)
    d = TreeNode(11)
    e = TreeNode(1)
    f = TreeNode(1)
    g = TreeNode(9)
    h = TreeNode(2)
    i = TreeNode(17)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h
    f.left = i