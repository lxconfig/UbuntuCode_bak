

"""
    给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

    思路：
        先中序遍历，再找第k个节点
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    # 运行时间：24ms  占用内存：5720k
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot:
            return None
        ret = self.InOrder(pRoot)
        if k > len(ret) or k <= 0:
            return None
        return ret[k-1]
        
    def InOrder(self, root):
        if not root:
            return None
        stack = []
        ret = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                ret.append(node)
                node = node.right
        return ret

if __name__ == "__main__":
    a = TreeNode(9)
    b = TreeNode(7)
    c = TreeNode(12)
    d = TreeNode(5)
    e = TreeNode(8)
    f = TreeNode(10)
    g = TreeNode(13)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    solution = Solution()

    print(solution.KthNode(a, 0))