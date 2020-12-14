

"""
    请实现两个函数，分别用来序列化和反序列化二叉树

    二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。
    序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。
    二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

    例如，我们可以把一个只有根节点为1的二叉树序列化为"1,"，然后通过自己的函数来解析回这个二叉树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 运行时间：28ms  占用内存：5752k
    def __init__(self):
        self.flag = -1
    
    def Serialize(self, root):
        # write code here
        if not root:
            return None
        ret = []
        def PreOrder(root, ret):
            if not root:
                ret.append("#,")
                return
            ret.append(str(root.val) + ",")
            PreOrder(root.left, ret)
            PreOrder(root.right, ret)
            return ret
        ret = PreOrder(root, ret)
        return "".join(ret)

    def Deserialize(self, s):
        # write code here
        if not s:
            return None
        self.flag += 1
        ss = s.split(",")
        if self.flag >= len(s):
            return None
        root = None
        if ss[self.flag] != "#":
            root = TreeNode(int(ss[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

    # def Inorder(self, root):
        # if not root:
        #     return None
        # stack, node = [], root
        # while stack or node:
        #     if node:
        #         stack.append(node)
        #         node = node.left
        #     else:
        #         node = stack.pop()
        #         print(node.val, end=" ")
        #         node = node.right

if __name__ == "__main__":
    a = TreeNode(8)
    b = TreeNode(7)
    c = TreeNode(4)
    d = TreeNode(3)
    e = TreeNode(9)
    f = TreeNode(6)
    g = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    solution = Solution()
    s = solution.Serialize(a)
    print(s)
    root = solution.Deserialize(s)
    # solution.Inorder(root)