

"""
    给定一个二叉树，找出其最大深度。
    二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """递归法（自底向上）
        分别计算出左子树的深度，右子树的深度，再计算其最大值
        最后+1，是加上根节点这一层
        """
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def maxDepth_1(self, root: TreeNode) -> int:
        """递归法（自顶向下）
        """
        def top_down(root, depth):
            if not root: return depth
            return max(top_down(root.left, depth+1), top_down(root.right, depth+1))
        return top_down(root, 0)

    def maxDepth_2(self, root: TreeNode) -> int:
        """层次遍历
        用二维数组来保存每一层的节点，如： [[3], [2, 4]...]
        最后返回二维数组的长度
        """
        if not root: return 0
        white, gray, init_level, ret = 0, 1, 0, []
        stack = [(white, root, init_level)]
        while stack:
            color, node, level = stack.pop()
            if color == white:
                stack.append((gray, node, level))
                stack.append((white, node.left, level+1))
                stack.append((white, node.right, level+1))
            else:
                if len(ret) == level: ret.append([])
                ret[level].append(node.val)
        return len(ret)