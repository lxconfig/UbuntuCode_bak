

"""
    操作给定的二叉树，将其变换为源二叉树的镜像。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # 运行时间：28ms 占用内存：5732k
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root


if __name__ == "__main__":
    pass