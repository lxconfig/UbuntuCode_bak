

"""
    给定一个排好序的数组，将其转换成一颗平衡的二叉搜索树
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def convert(array):
    arrayLen = len(array)
    if arrayLen == 0:
        return None
    
    mid = arrayLen // 2
    root = TreeNode(array[mid])

    root.left = convert(array[:mid])
    root.right = convert(array[mid+1:])
    return root


def PreOrder(root):
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


def InOrder(root):
    if not root:
        return None
    stack = []
    node = root
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.value, end=" ")
            node = node.right


def PostOrder(root):
    if not root:
        return None
    stack = [root]
    while stack:
        node = stack[-1]
        if node.right == None and node.left == None:
            print(stack.pop().value, end=" ")
        else:
            if node.right:
                stack.append(node.right)
                node.right = None
            if node.left:
                stack.append(node.left)
                node.left = None
        
        
if __name__ == "__main__":
    array = [-10, -3, 0, 5, 9]
    root = convert(array)
    PreOrder(root)
    print()
    InOrder(root)
    print()
    PostOrder(root)