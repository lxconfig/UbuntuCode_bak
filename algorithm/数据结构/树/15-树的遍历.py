

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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
    while stack or node:
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
        if node.left == None and node.right == None:
            print(stack.pop().value, end=" ")
        else:
            if node.right:
                stack.append(node.right)
                node.right = None
            if node.left:
                stack.append(node.left)
                node.left = None


def BFS(root):
    if not root:
        return None
    stack = [root]
    while stack:
        node = stack.pop(0)
        print(node.value, end=" ")
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    

def DFS(self, root):
    if not root: return None
    stack = [root]
    ret = []
    while stack:
        node = stack.pop()
        ret.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return ret


if __name__ == "__main__":
    a = TreeNode(8)
    b = TreeNode(4)
    c = TreeNode(10)
    d = TreeNode(3)
    e = TreeNode(5)
    f = TreeNode(9)
    g = TreeNode(14)
    h = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h
    PreOrder(a)
    print()
    InOrder(a)
    print()
    BFS(a)
    print()
    PostOrder(a)