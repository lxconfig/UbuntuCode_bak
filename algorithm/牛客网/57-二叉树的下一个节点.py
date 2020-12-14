

"""
    给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
    
    思路：列举所有的情况
        1. 叶子节点
            1.1 如果pNode是左子树的叶子节点，则下一个节点一定是其父节点。特别的，当是左子树最右边的节点时，下一个节点是根节点
            1.2 如果pNode是右子树的叶子节点，则下一个节点一定是根节点。特别的，当是右子树最右边的节点时，下一个节点为空
            1.3 如果只有一个节点，则下一个节点为空
        
        2. 只有左孩子
            下一个节点一定是父节点
        
        3. 只有右孩子
            下一个节点一定是右孩子
        
        4. 既有左孩子又有右孩子
            4.1 如果pNode是根节点，则下一个节点一定是右子树的最左边的节点
            4.2 否则，下一个节点一定是右孩子
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        # 运行时间：24ms  占用内存：5848k
        if not pNode:
            return None
        
        if pNode.left == None and pNode.right == None:
            # 叶子节点
            if pNode.next == None:
                # 叶子节点，且只有一个节点
                return None
            if pNode.next.left == pNode:
                # 左边节点
                return pNode.next.val
            else:
                node = pNode
                # 找到根节点
                while node.next:
                    node = node.next
                n = node
                while n.right:
                    n = n.right
                if n.val == pNode.val:
                    # 右子树最右边的节点
                    return None
                else:
                    # 左子树最右边的节点
                    return node.val
        
        elif pNode.left == None and pNode.right != None:
            # 有右孩子
            return pNode.right.val
        elif pNode.left != None and pNode.right == None:
            # 有左孩子
            return pNode.next.val
        else:
            # 既有左孩子又有右孩子
            if not pNode.next:
                # 根节点
                node = pNode
                parent = None
                while node.right:
                    node = node.right
                    if node.left and node.right:
                        parent = node
                # 右子树最左边的节点
                parent = parent.left
                return parent.val
            else:
                return pNode.right.val


    def GetNext2(self, pNode):
        """
            1. 如果pNode有右子树，则找到右子树最左边的节点，就是pNode的下一个节点
            2. 如果pNode没有右子树，则分两种情况：
                2.1 如果pNode是左侧的节点，下一个节点就是pNode的父节点
                2.2 如果pNode是右侧的节点，则要向上找，直到找到某个父节点的左孩子=pNode(每找一次，pNode要变化成其父节点)，到根节点还不满足的话，说明没有下一个节点
        """
        # 运行时间：26ms  占用内存：5852k
        if not pNode:
            return None
        if pNode.right:
            # 有右子树,找右子树最左边的节点
            node = pNode.right
            while node.left:
                node = node.left
            return node
        # 没有右子树
        while pNode.next:
            if pNode.next.left == pNode:
                return pNode.next
            pNode = pNode.next
        return None

    def GetNext3(self, pNode):
        """先找到根节点，再中序遍历，找下一个节点
        """
        # 运行时间：25ms  占用内存：5860k
        if not pNode:
            return None
        node = pNode
        while node.next:
            node = node.next
        stack = []
        ret = []
        p = node
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                ret.append(p)
                p = p.right
        if len(ret) == 1:
            return None

        for i in range(len(ret)):
            if ret[i] == pNode and i != len(ret) - 1:
                return ret[i+1]
        return None


if __name__ == "__main__":
    a = TreeLinkNode(8)
    b = TreeLinkNode(6)
    c = TreeLinkNode(10)
    d = TreeLinkNode(5)
    e = TreeLinkNode(7)
    f = TreeLinkNode(9)
    g = TreeLinkNode(11)
    h = TreeLinkNode(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    # d.left = h
    b.next = a
    c.next = a
    d.next = b
    e.next = b
    f.next = c
    g.next = c
    # h.next = d
    solution = Solution()
    print(solution.GetNext3(a))