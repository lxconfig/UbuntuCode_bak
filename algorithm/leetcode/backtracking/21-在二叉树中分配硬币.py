# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        def dfs(node):
            if not node: return 0
            # 优先考虑左右子树，使它们先满足条件，再计算根节点
            left = dfs(node.left)  # 要使左子树满足条件，需要拿走的金币数，可能是0，正数或负数
            self.res += abs(left)  # 拿走的金币数即移动次数
            right = dfs(node.right)
            self.res += abs(right)
            # 对某颗子树的根节点来说，要从它这拿走的金币数就是 node.val + left + right - 1
            return node.val + left + right - 1
        dfs(root)
        return self.res