
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def PreOrder(root):
    """前序遍历
    """
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
    """中序遍历
    """
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
        if node.left == None and node.right == None:
            print(stack.pop().value, end=" ")
        if node.right:
            stack.append(node.right)
            node.right = None
        if node.left:
            stack.append(node.left)
            node.left = None


def BFS(root):
    """广度优先遍历
    """
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


""" 颜色标记法 """
def PreOrderTraversal(root):
    if not root: return None
    white, gray, ret = 0, 1, []
    stack = [(white, root)]
    while stack:
        color, node = stack.pop()
        if not node: continue
        if color == white:
            stack.append((white, node.right))
            stack.append((white, node.left))
            stack.append((gray, node))            
        else:
            ret.append(node.value)
    return ret


def InOrderTraversal(root):
    """
    将white为TreeNode数据类型，gray为int数据类型
        stack,rst = [root],[]
        while stack:
            i = stack.pop()
            if isinstance(i,TreeNode):
                stack.extend([i.right,i.val,i.left])
            elif isinstance(i,int):
                rst.append(i)
        return rst
    """
    if not root: return None
    white, gray, ret = 0, 1, []
    stack = [(white, root)]
    while stack:
        color, node = stack.pop()
        if not node: continue
        if color == white:
            # 白色表示没有访问过的节点
            stack.append((white, node.right))
            stack.append((gray, node))
            stack.append((white, node.left))
        else:
            # 灰色表示访问过
            ret.append(node.value)
    return ret


def PostOrderTraversal(root):
    if not root: return None
    white, gray, ret = 0, 1, []
    stack = [(white, root)]
    while stack:
        color, node = stack.pop()
        if not node: continue
        if color == white:
            stack.append((gray, node))
            stack.append((white, node.right))
            stack.append((white, node.left))
        else:
            ret.append(node.value)
    return ret


def levelOrder(root):
    """层次遍历 BFS
    """
    if not root: return None
    white, gray, ret = 0, 1, []
    stack = [(white, root)]
    while stack:
        color, node = stack.pop(0)
        if not node: continue
        if color == white:
            stack.append((gray, node))
            stack.append((white, node.left))
            stack.append((white, node.right))
        else:
            ret.append(node.value)
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
    # PreOrder(a)
    # print()
    # InOrder(a)
    # print()
    # # PostOrder(a)
    # # print()
    # BFS(a)


    print(PreOrderTraversal(a))
    print(InOrderTraversal(a))
    print(PostOrderTraversal(a))
    print(levelOrder(a))