
"""
    请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

    思路:
        用两个栈分别存放奇数层和偶数层的节点
"""



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # 运行时间：34ms  占用内存：5856k
        if not pRoot:
            return []
        odd, even, ret = [], [pRoot], []
        while odd or even:
            tmps = []
            tmp = []
            while even:
                node = even.pop()
                tmps.append(node.val)
                if node.left:
                    odd.append(node.left)
                if node.right:
                    odd.append(node.right)
            if tmps:
                ret.append(tmps)
            
            while odd:
                node = odd.pop()
                tmp.append(node.val)
                if node.right:
                    even.append(node.right)
                if node.left:
                    even.append(node.left)
            if tmp:
                ret.append(tmp)
        return ret


if __name__ == "__main__":
    a = TreeNode(8)
    b = TreeNode(7)
    c = TreeNode(4)
    d = TreeNode(3)
    e = TreeNode(9)
    f = TreeNode(6)
    g = TreeNode(5)
    h = TreeNode(11)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    f.left = h

    solution = Solution()
    print(solution.Print(a))