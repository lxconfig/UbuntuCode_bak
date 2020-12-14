
"""
    给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list:
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
        tmp = [sum(i) / len(i) for i in ret]
        return tmp


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

    print(s.averageOfLevels(a))