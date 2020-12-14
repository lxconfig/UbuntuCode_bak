

"""
    输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        ret = []

        def _FindPath(root, path, curSum):
            curSum += root.val
            path.append(root)
            # if not root.left and not root.right:
            #     # 叶子节点
            #     if curSum == expectNumber:
            #         # 找到一条路径
            #         onePath = []
            #         for node in path:
            #             onePath.append(node.val)
            #         ret.append(onePath)
            #     if curSum < expectNumber:
            #         if root.left:
            #             _FindPath(root.left, path, curSum)
            #         if root.right:
            #             _FindPath(root.right, path, curSum)
            # else:
            #         if root.left:
            #             _FindPath(root.left, path, curSum)
            #         if root.right:
            #             _FindPath(root.right, path, curSum)
            isLeaf = root.left == None and root.right == None  # 叶子节点
            if curSum == expectNumber and isLeaf:
                # 找到一条路径
                onePath = []
                for node in path:
                    onePath.append(node.val)
                ret.append(onePath)
            if curSum < expectNumber:
                if root.left:
                    _FindPath(root.left, path, curSum)
                if root.right:
                    _FindPath(root.right, path, curSum)
            path.pop()
        
        _FindPath(root, [], 0)
        return ret


if __name__ == "__main__":
    a = TreeNode(8)
    b = TreeNode(4)
    c = TreeNode(5)
    d = TreeNode(7)
    e = TreeNode(3)
    f = TreeNode(2)
    g = TreeNode(9)
    h = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h
    solution = Solution()
    print(solution.FindPath(a, 15))

