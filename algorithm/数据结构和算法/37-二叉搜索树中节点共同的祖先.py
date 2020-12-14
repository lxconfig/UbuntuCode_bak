

"""
    给定一颗二叉搜索树，再给定其中的两个节点p,q，找到这两个节点最近的共同祖先
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findCommonAncestor(root, p, q):
    if not root:
        return None
    
    while root:
        # p,q都比root小，就去左边找
        if p.value < root.value and q.value < root.value:
            root = root.left
        # p,q都比root大，就去右边找
        elif p.value > root.value and q.value > root.value:
            root = root.right
        # 一个大一个小，或者一个小一个大，或者相等，都表示root就是结果
        else:
            return root.value


if __name__ == "__main__":
    a = TreeNode(8)
    b = TreeNode(4)
    c = TreeNode(10)
    d = TreeNode(3)
    e = TreeNode(5)
    f = TreeNode(9)
    g = TreeNode(14)
    h = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h
    print(findCommonAncestor(a, h, e))
    print(findCommonAncestor(a, h, f))
    print(findCommonAncestor(a, e, f))
    print(findCommonAncestor(a, f, g))
    print(findCommonAncestor(a, b, e))