

"""
    输入两个链表，找出它们的第一个公共结点。

    思路：按照链表排序来做
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # 运行时间：22ms  占用内存：5864k
        # ret = []
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                # ret.append(pHead1.val)
                pHead1 = pHead1.next
            elif pHead1.val > pHead2.val:
                # ret.append(pHead2.val)
                pHead2 = pHead2.next
            else:
                return pHead1
        return None


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(5)

    d = ListNode(2)
    e = ListNode(4)
    f = ListNode(5)

    a.next = b
    b.next = c

    d.next = e
    e.next = f
    solution = Solution()
    print(solution.FindFirstCommonNode(a, d))