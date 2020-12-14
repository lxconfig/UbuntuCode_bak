

"""
    根据一棵树的中序遍历与后序遍历构造二叉树。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        if not inorder or not postorder: return 

        root = TreeNode(postorder[-1])
        root_index = inorder.index(root.val)

        # 中序遍历 左右子树
        inorder_left = inorder[0: root_index]
        inorder_right = inorder[root_index + 1: ]

        # 后序遍历 左右子树
        postorder_left = postorder[0: root_index]
        postorder_right = postorder[root_index: -1]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        return root


if __name__ == "__main__":
    s = Solution()
    postorder = [9,15,7,20,3]
    inorder = [9,3,15,20,7]
    print(s.buildTree(inorder, postorder))