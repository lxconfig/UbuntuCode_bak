class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def isCycle(head):
    """判断链表中是否有环"""
    # 采用双指针，一个快(每次走两步)，一个慢(每次走一步)
    fast = slow = head
    while fast and slow and fast.next:
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            # 有环
            return True
    return False


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(0)
    c = ListNode(3)
    d = ListNode(8)
    e = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    print(isCycle(a))