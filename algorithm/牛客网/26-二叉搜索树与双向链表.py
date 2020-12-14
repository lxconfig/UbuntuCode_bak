

"""
    输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

    思路：按中序遍历得到排序的结果，然后改变左右指针
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # 运行时间：23ms  占用内存：5864k
        if not pRootOfTree:
            return None
        stack = []
        inOrder = []
        node = pRootOfTree
        # while True:
        #     while node:
        #         stack.append(node)
        #         node = node.left
        #     if len(stack) == 0:
        #         break
        #     node = stack.pop()
        #     inOrder.append(node)
        #     node = node.right
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                inOrder.append(node)
                node = node.right
        # return inOrder
        ret = inOrder[0]
        while inOrder:
            curNode = inOrder.pop(0)
            if inOrder:
                # 最后一个元素没有right
                curNode.right = inOrder[0]
                inOrder[0].left = curNode
        return ret
        

if __name__ == "__main__":
    a = TreeNode(9)
    b = TreeNode(4)
    c = TreeNode(15)
    d = TreeNode(2)
    e = TreeNode(5)
    f = TreeNode(12)
    g = TreeNode(17)
    h = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h
    solution = Solution()
    print(solution.Convert(a))