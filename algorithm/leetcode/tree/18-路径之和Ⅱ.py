

"""
    给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> list:
        if not root: return []
        stack, ret = [([root.val], root)], []
        while stack:
            value, node = stack.pop()
            # print(value)
            if not node.left and not node.right and sum(value) == target:
                ret.append(value)
                # return True
            if node.right:
                stack.append((value + [node.right.val], node.right))
            if node.left:
                stack.append((value + [node.left.val], node.left))
        return ret

    def pathSum_1(self, root: TreeNode, target: int) -> list:
        """负数的情况不好判断
        """
        if not root: return []
        curSum, ret, path = 0, [], []
        
        def helper(root, curSum, path):
            curSum += root.val
            path.append(root.val)
            isLeaf = True if not root.left and not root.right else False
            if curSum == target and isLeaf:
                onepath = []
                for node in path:
                    onepath.append(node)
                ret.append(onepath)
            if abs(curSum) < abs(target):  # 负数的情况  [-2,null,-3]  -5
                if root.left:
                    helper(root.left, curSum, path)
                if root.right:
                    helper(root.right, curSum, path)
            path.pop()
        helper(root, curSum, path)
        return ret



if __name__ == "__main__":
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(8)
    d = TreeNode(11)
    e = TreeNode(13)
    f = TreeNode(4)
    g = TreeNode(7)
    h = TreeNode(2)
    i = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    c.left = e
    c.right = f
    d.left = g
    d.right = h
    f.right = i
    s = Solution()
    print(s.pathSum_1(a, 22))