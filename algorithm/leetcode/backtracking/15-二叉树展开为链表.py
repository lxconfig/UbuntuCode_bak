
"""
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """通过前序遍历链接节点
        """
        preOrder_list = []
        def pre_order(root):
            if not root: return 
            preOrder_list.append(root)
            pre_order(root.left)
            pre_order(root.right)
        
        pre_order(root)
        for i in range(1, len(preOrder_list)):
            prev_node, cur_node = preOrder_list[i - 1], preOrder_list[i]
            prev_node.left = None
            prev_node.right = cur_node

    def flatten_1(self, root: TreeNode) -> None:
        """在遍历途中，记录prev的节点
        """
        stack, prev_node = [root], None
        while stack:
            cur_node = stack.pop()
            if prev_node:
                prev_node.left = None
                prev_node.right = cur_node
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
            prev_node = cur_node

