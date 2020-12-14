import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """二叉搜索树"""
    def __init__(self, root=None):
        self.root = root
    
    def get(self, value):
        """查找某个值是否在树中"""
        return self.__get(self.root, value)

    def __get(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if node.value < value:
            return self.__get(node.right, value)
        else:
            return self.__get(node.left, value)
    
    def IterativeGet(self, value):
        """非递归版 查找某个值是否在树中"""
        return self.__IterativeGet(self.root, value)

    def __IterativeGet(self, node, value):
        if not node:
            return False
        while node:
            if value == node.value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return False
            
    def add(self, value):
        """插入一个节点到树中"""
        self.root = self.__add(self.root, value)
    
    def __add(self, node, value):
        if node is None:
            return Node(value)
        if node.value == value:
            pass
        if value < node.value:
            node.left = self.__add(node.left, value)
        else:
            node.right = self.__add(node.right, value)
        return node

    def IterativeAdd(self, value):
        """非递归版 插入节点到树中"""
        return self.__IterativeAdd(self.root, value)

    def __IterativeAdd(self, node, value):
        newNode = Node(value)
        if not node:
            node = newNode
            return "OK"
        parentNode = None
        while True:
            parentNode = node
            if value == node.value:
                return "already exist" 
            if value < node.value:
                node = node.left
                if not node:
                    parentNode.left = newNode
                    return "OK"
            else:
                node = node.right
                if not node:
                    parentNode.right = newNode
                    return "OK"

    def PreOrder(self, root):
        """先序遍历"""
        if not root:
            return None
        print(root.value, end=" ")
        self.PreOrder(root.left)
        self.PreOrder(root.right)

    def IterativePreOrder(self, root):
        """非递归版 先序遍历"""
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            print(node.value, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
    def InOrder(self, root):
        """中序遍历"""
        if not root:
            return None
        self.InOrder(root.left)
        print(root.value, end=" ")
        self.InOrder(root.right)
    
    def IterativeInOrder(self, root):
        """非递归版 中序遍历"""
        if not root:
            return None
        stack = []
        node = root
        # while True:
        #     while node:
        #         stack.append(node)
        #         node = node.left
        #     if len(stack) == 0:
        #         return 
        #     # 退出上面的循环表示，node已经为None，到达了最左边
        #     node = stack.pop()
        #     print(node.value, end=" ")
        #     node = node.right
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(node.value, end=" ")
                node = node.right
    
    def PostOrder(self, root):
        """后序遍历"""
        if not root:
            return None
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.value, end=" ")
    
    def IterativePostOrder(self, root):
        """这种写法改变了树的结构
        经过此后序遍历后，原树只包含根节点
        """
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack[-1]
            if not node.left and not node.right:
                print(stack.pop().value, end=" ")
            else:
                if node.right:
                    stack.append(node.right)
                    node.right = None
                if node.left:
                    stack.append(node.left)
                    node.left = None
    
    # def IterativePostOrder2(self, root):
    #     stack = [(root, False)]
    #     while stack:
    #         node, visited = stack.pop()
    #         if node:
    #             if visited:
    #                 print(node.value, end=" ")
    #         else:
    #             stack.append((node, True))
    #             stack.append((node.right, False))
    #             stack.append((node.left, False))
                
    
    def BFS(self, root):
        """层次遍历"""
        if not root:
            return None
        queue = [root]
        while queue:
            curNode = queue.pop(0)
            print(curNode.value, end=" ")
            if curNode.left:
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)

    def get_max(self, root):
        """获取树中最大值"""
        if not root:
            return None
        while root.right:
            root = root.right
        return root.value
    
    def get_min(self, root):
        """获取树中最小值"""
        if not root:
            return None
        if root.left:
            return self.get_min(root.left)
        else:
            return root.value

    def remove(self, key):
        """删除树中的一个节点
        删除一个节点A，有四种情况：
            (1) 节点A没有孩子节点。此时直接将节点A改为None即可
            (2) 节点A有左孩子或者右孩子。此时直接将左孩子或右孩子的值复制给节点A
            (3) 节点A既有左孩子又有右孩子。此时只要再右子树中找到最小值节点或者再左子树中找到最大值节点，把其值复制给节点A，再删除掉最值节点即可
            (4) 节点A不存在。直接返回None
        """ 
        self.root = self.__remove(self.root, key)

    def __remove(self, node, key):
        if node is None:
            return None
        if key < node.value:
            node.left = self.__remove(node.left, key)   # node.left = 相当于连接两个节点
        elif key > node.value:
            node.right = self.__remove(node.right, key)
        else:
            # 找到了
            if node.left is None:
                # 说明只有右孩子或者没有孩子
                node = node.right
            elif node.right is None:
                # 说明只有左孩子或者没有孩子
                node = node.left
            else:
                # 有左右孩子
                node.value = self.get_min(node.right)   # 在右子树中找一个最小值替换过来(只复制value)
                node.right = self.__remove(node.right, node.value)   # 在删掉最小值的节点
        return node

    def size(self):
        """获取树的大小"""
        return self.__size(self.root)
    
    def __size(self, node):
        if node is None:
            return 0
        return 1 + self.__size(node.left) + self.__size(node.right)
    
    def maxDepth(self):
        """获取树的最大深度"""
        return self.__maxDepth(self.root)
    
    def __maxDepth(self, node):
        if node is None:
            return 0
        return 1 + max(self.__maxDepth(node.left), self.__maxDepth(node.right))

    def floor(self, key):
        """当key存在时，返回key值
        当key不存在时，返回小于key的最后一个值
        如：10 6 14 4 8 12 16，key=15
        返回14
        """
        return self.__floor(self.root, key)

    def __floor(self, node, key):
        if not node:
            return None
        if key == node.value:
            return node.value
        if key < node.value:
            return self.__floor(node.left, key)
        t = self.__floor(node.right, key)
        if t:
            return t
        return node.value
    
    def celling(self, key):
        """当key存在时，返回key值
        当key不存在时，返回大于key的第一个值
        如：10 6 14 4 8 12 16，key=15
        返回16
        """
        return self.__celling(self.root, key)

    def __celling(self, node, key):
        if not node:
            return None
        if key == node.value:
            return node.value
        if key > node.value:
            return self.__celling(node.right, key)
        t = self.__celling(node.left, key)
        if t:
            return t
        return node.value
    
    def isBST(self):
        """判断一棵树是不是BST"""
        return self.__isBST(self.root, -sys.maxsize, sys.maxsize)

    def __isBST(self, node, minval, maxval):
        if not node:
            return True
        # 如果一个节点的值比最小值还要小，或者比最大值还要大，那肯定不是BST
        # minval 和 maxval表示取值范围的最小值和最大值
        # 可以理解为负无穷和正无穷
        if node.value < minval or node.value > maxval:
            return False
        return self.__isBST(node.left, minval, node.value) and self.__isBST(node.right, node.value, maxval)

if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.add(8)
    bst.add(4)
    bst.add(9)
    bst.add(3)
    bst.add(13)
    # print(bst.get(90))
    # print("树的初始大小:", bst.size())
    # print("树的最大深度:", bst.maxDepth())
    # bst.PreOrder(bst.root)
    # print()
    # bst.InOrder(bst.root)
    # print()
    # bst.PostOrder(bst.root)
    # print()
    # print(bst.get_max(bst.root))
    # print(bst.get_min(bst.root))
    # bst.remove(8)
    # bst.PreOrder(bst.root)
    # print()
    # print("树的大小:", bst.size())
    # print(bst.floor(5))
    # print(bst.celling(12))
    # print(bst.isBST())
    # print(bst.IterativeGet(22))
    print(bst.IterativeAdd(2))
    print(bst.IterativeAdd(10))
    print(bst.IterativeAdd(22))
    # bst.BFS(bst.root)
    # print()
    bst.IterativeInOrder(bst.root)
    print()
    bst.IterativePreOrder(bst.root)
    print()
    bst.IterativePostOrder(bst.root)
    