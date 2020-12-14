

"""
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int):
        """递归法
            1. 对于n=0时，可以直接返回[]
            2. 定义build_tree(left, right)函数，表示生成[left,...,right]之间所有可能的二叉搜索树
                2.1 若 left > right, 不满足二叉搜索树的定义，返回[None]
                2.2 遍历[left, right+1)范围内所有数：
                    2.2.1 所有可能的左子树列表left_tree = build_tree(left, i-1)
                    2.2.2 所有可能的右子树列表right_tree = build_tree(i+1, right)
                    2.2.3 组合所有的方式，遍历左子树和右子树列表：
                        - 生成当前数的节点TreeNode(i)
                        - 将其左子树置为l
                        - 将其右子树置为r
        """
        if not n or n == 0: return []
        def build_tree(left, right):
            if left > right: return [None]
            all_trees = []
            for i in range(left, right+1):
                left_tree = build_tree(left, i-1)
                right_tree = build_tree(i+1, right)
                for lnode in left_tree:
                    for rnode in right_tree:
                        cur_tree_node = TreeNode(i)
                        cur_tree_node.left = lnode
                        cur_tree_node.right = rnode
                        all_trees.append(cur_tree_node.val)
                print(all_trees)
            return all_trees
        res = build_tree(1, n)
        return res


    def generateTrees_2(self, n: int):
        if n == 0:
            return None
        # 对dp进行初始化
        dp = []
        for i in range(0, n+1):   # 初始化dp
            dp.append([])
            for j in range(0, n+1):
                if i == j:
                    dp[i].append([TreeNode(i).val])
                elif i < j:
                    dp[i].append([])
                else:
                    dp[i].append([None])
        dp[0][0] = [None]
        for i in range(n-1, 0, -1):  # 自下向上进行循环
            for j in range(i+1, n+1):
                for r in range(i, j+1):   # i-j每一个节点为顶点的情况
                    left = r+1 if r < j else r    # 右边的值需要边界判断，不然会溢出数组
                    for x in dp[i][r-1]:          # 左右子树排列组合   
                        for y in dp[left][j]:
                            node = TreeNode(r)     
                            node.left = x
                            node.right = y
                            if r == j:
                                node.right = None
                            dp[i][j].append(node.val)      # dp[i][j]添加此次循环的值
        print(dp)
        return dp[1][n]


if __name__ == "__main__":
    s = Solution()
    print(s.generateTrees_2(3))