
"""
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        """路径总和
        """
        if not root: return False
        def dfs(node, target):
            # 终止条件
            if not node: return False
            target -= node.val
            if not node.left and not node.right and target == 0:
                return True
            return dfs(node.left, target) or dfs(node.right, target)
        return dfs(root, target)
    

    def pathSum_1(self, root: TreeNode, target: int) -> List[List[int]]:
        """路径总和Ⅱ
        """
        # DFS 回溯
        res, path = [], []
        def dfs(node, target, res, path):
            # 终止条件
            if not node: return
            path.append(node.val)
            target -= node.val
            if not node.left and not node.right and target == 0:
                res.append(path[:])
            dfs(node.left, target, res, path)
            dfs(node.right, target, res, path)
            path.pop()
        dfs(root, target, res, path)
        return res
    
    def pathSum_3(self, root: TreeNode, target: int) -> int:
        """路径总和Ⅲ
        在遍历过程中，每搜索到一个新节点，都计算一次从根节点到当前节点的路径和(curSum)，并存储在哈希表中
        寻找子路径的判断：当前路径和 - target是否在哈希表中存储过
        """
        from collections import defaultdict
        hash_table = defaultdict(int)
        hash_table[0] = 1  # 防止从根节点开始的路径和=target时找不到
        def dfs(node, curSum):
            if not node: return 0
            curSum += node.val
            count = hash_table[curSum - target]
            hash_table[curSum] += 1
            left_count = dfs(node.left, curSum)
            right_count = dfs(node.right, curSum)
            hash_table[curSum] -= 1
            return left_count + right_count + count
        return dfs(root, 0)


if __name__ == "__main__":
    s = Solution()
    a = TreeNode(1)
    b = TreeNode(-2)
    c = TreeNode(-3)
    # d = TreeNode(11)
    # e = TreeNode(13)
    # f = TreeNode(4)
    # g = TreeNode(7)
    # h = TreeNode(2)
    # i = TreeNode(5)
    # j = TreeNode(1)
    a.left, a.right = b, c
    # b.left = d
    # c.left, c.right = e, f
    # d.left, d.right = g, h
    # f.left, f.right = i, j
    print(s.pathSum_3(a, -1))