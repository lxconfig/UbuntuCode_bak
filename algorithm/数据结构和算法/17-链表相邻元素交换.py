import pysnooper

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# @pysnooper.snoop(output="./log.log", overwrite=True)
def swapPairs(head):
    """交换链表中相邻的两个元素"""
    tmp = ListNode(-1)
    tmp.next = head
    cur = tmp
    while cur.next and cur.next.next:
        # f和t要始终指向当前需要交换的节点
        f = cur.next.next
        t = cur.next
        cur.next = f
        t.next = f.next
        f.next = t
        cur = cur.next.next
    return tmp.next.val


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
    print(swapPairs(a))