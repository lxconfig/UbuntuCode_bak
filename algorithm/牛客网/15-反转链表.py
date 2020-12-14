

"""
    输入一个链表，反转链表后，输出新链表的表头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        # 运行时间：36ms  占用内存：5856k
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead
        l = pHead
        m = pHead.next
        r = m.next
        l.next = None
        while r:
            m.next = l
            l = m
            m = r
            r = r.next
        m.next = l
        return m


if __name__ == "__main__":
    solution = Solution()

    a = ListNode(1)
    b = ListNode(0)
    c = ListNode(3)
    d = ListNode(8)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    print(solution.ReverseList(a))