
"""
    输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        # 运行时间：29ms  占用内存：5720k
        # 减少循环后：运行时间：22ms  占用内存：5740k
        pHead3 = ListNode(-1)
        t = pHead3
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                t.next = pHead1
                pHead1 = pHead1.next
                t = t.next
            else:
                t.next = pHead2
                pHead2 = pHead2.next
                t = t.next

        # 若任意一方没有元素了，直接把另一方剩下的元素添加进来，不需要循环
        if pHead1:
            t.next = pHead1
        elif pHead2:
            t.next = pHead2
        # while pHead1:
        #     t.next = pHead1
        #     pHead1 = pHead1.next
        #     t = t.next

        # while pHead2:
        #     t.next = pHead2
        #     pHead2 = pHead2.next
        #     t = t.next

        return pHead3.next


if __name__ == "__main__":
    pass