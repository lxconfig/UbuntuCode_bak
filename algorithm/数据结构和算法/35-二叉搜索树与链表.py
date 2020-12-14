
"""
    给定一个有序链表，将其重建为二叉搜索树
    
    思路：找到链表的中间节点，作为树的根节点，然后链表前一部分和后一部分分别递归
"""


class LinkNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def convert(head):
    if not head:
        return None
    # 当只有一个节点时，直接返回
    if not head.next:
        return TreeNode(head.value)
    
    # 快慢指针法，取到中间节点
    fast = slow = left_tail = head
    while fast and fast.next:
        fast = fast.next.next
        left_tail = slow
        slow = slow.next

    left_tail.next = None
    root = TreeNode(slow.value)
    
    root.left = convert(head)
    root.right = convert(slow.next)
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
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == "__main__":
    a = LinkNode(1)
    b = LinkNode(2)
    c = LinkNode(3)
    d = LinkNode(4)
    e = LinkNode(5)
    f = LinkNode(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    root = convert(a)
    PreOrder(root)
    print()
    InOrder(root)
    print()
    # PostOrder(root)
    # print()
    BFS(root)
