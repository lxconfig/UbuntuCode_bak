


"""
    给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        """BFS
            最后得到结果翻转一下即可
        """
        if not root: return []
        queue, ret = [(0, root)], []
        while queue:
            level, node = queue.pop(0)
            if len(ret) == level: ret.append([])
            ret[level].append(node.val)
            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))
        return ret[::-1]

    def levelOrderBottom_2(self, root: TreeNode) -> list:
        """DFS
            最后得到结果翻转一下即可
        """
        if not root: return []
        stack, ret = [(0, root)], []
        while stack:
            level, node = stack.pop()
            if len(ret) == level: ret.append([])
            ret[level].append(node.val)
            if node.right:
                stack.append((level + 1, node.right))
            if node.left:
                stack.append((level + 1, node.left))
        return ret[::-1]


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

    print(s.levelOrderBottom_2(a))