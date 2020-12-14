

"""
    请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        """求出原二叉树的前序遍历，及镜像二叉树的前序遍历
        如果相等则说明是对称二叉树
        注：不能用中序遍历，当二叉树中所有节点的值都相同时，中序遍历的结果都是一样的
        """
        # 运行时间：25ms  占用内存：5736k
        if not pRoot:
            return True
        ret1 = self.PreOrder([], pRoot)
        root = self.Mirror(pRoot)
        ret2 = self.PreOrder([], root)
        return ret1 == ret2
        # return self.helper(pRoot, root)

    def Mirror(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
    
    def PreOrder(self, ret, root):
        """对于没有左孩子或右孩子或叶子节点
        需要补上没有的节点，防止所有节点值相等时，遍历没有效果
        """
        if not root:
            ret.append(-1)
            return 
        ret.append(root.val)
        self.PreOrder(ret, root.left)
        self.PreOrder(ret, root.right)
        return ret

    
    def isSymmetrical2(self, pRoot):
        """递归比较法
        左子树的左节点和右子树的右节点比较
        左子树的右节点和右子树的左节点比较
        """
        if not pRoot:
            return True
        return self.compare(pRoot.left, pRoot.right)
        
    def compare(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            if self.compare(root1.left, root2.right) and self.compare(root1.right, root2.left):
                return True
        return False


if __name__ == "__main__":
    a = TreeLinkNode(5)
    b = TreeLinkNode(5)
    c = TreeLinkNode(5)
    d = TreeLinkNode(5)
    e = TreeLinkNode(5)
    f = TreeLinkNode(5)
    g = TreeLinkNode(5)
    a.left = b
    a.right = c
    b.left = d
    # b.right = e
    # c.left = f
    c.right = e
    d.left = f
    e.left = g
    solution = Solution()
    print(solution.isSymmetrical2(a))