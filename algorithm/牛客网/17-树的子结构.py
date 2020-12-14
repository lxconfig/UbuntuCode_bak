
"""
    输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # 通过先序遍历，转成字符串来判断
        # 运行时间：21ms  占用内存：5860k
        if not pRoot2:
            return False
        str1 = self.PreOrder(pRoot1)
        str2 = self.PreOrder(pRoot2)
        if str1.find(str2) == -1:
            return False
        else:
            return True

    def PreOrder(self, root):
        re = ""
        if not root:
            return ""
        re += str(root.value)
        if root.left or root.right:
            re += self.PreOrder(root.left)
            re += self.PreOrder(root.right)
        return re

    def HasSubtree2(self, pRoot1, pRoot2):
        """用来判断第一个节点是否相等"""
        # 运行时间：23ms  占用内存：5864k
        # 递归，一个一个判断
        ret = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                ret = self.helper(pRoot1, pRoot2)
            if not ret:
                # 如果第一个节点不同，那么比较树A的左子树和树B的第一个节点
                ret = self.HasSubtree2(pRoot1.left, pRoot2)
            if not ret:
                # 如果树A的左子树节点和树B的第一个节点也不同，就比较树A的右子树节点和树B的第一个节点
                ret = self.HasSubtree2(pRoot1.right, pRoot2)
        return ret
    
    def helper(self, root1, root2):
        """用来进一步判断左右子树是否相等"""
        # 一定要先判断root2，因为当root2为空时，才表示树B的子树已经判断完
        # 而如果是root1为空的话，表示的是树A已经没有节点，而树B还有，树B就肯定不是子结构
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        return self.helper(root1.left, root2.left) and self.helper(root1.right, root2.right)

if __name__ == "__main__":
    pass