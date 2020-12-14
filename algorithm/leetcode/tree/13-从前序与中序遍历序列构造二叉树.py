
"""
    根据一棵树的前序遍历与中序遍历构造二叉树。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        else:
            root = TreeNode(preorder[0])
            # print(root.val)
            root_index = inorder.index(root.val)

            # # 左子树
            # inorder_left = inorder[0: root_index]
            # preorder_left = preorder[1: root_index + 1]

            # # 右子树
            # inorder_right = inorder[root_index+1: ]
            # preorder_right = preorder[root_index+1: ]

            # root.left = self.buildTree(preorder_left, inorder_left)
            # root.right = self.buildTree(preorder_right, inorder_right)

            root.left = self.buildTree(preorder[1: root_index + 1], inorder[0: root_index])
            root.right = self.buildTree(preorder[root_index+1: ], inorder[root_index+1: ])
        return root


if __name__ == "__main__":
    s = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    print(s.buildTree(preorder, inorder))