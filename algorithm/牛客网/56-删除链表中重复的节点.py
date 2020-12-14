

"""
    在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

    思路：
        两指针法
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # 运行时间：23ms  占用内存：5860k
        if not pHead:
            return None
        if not pHead.next:
            return pHead
        head = ListNode(0)
        head.next = pHead
        f, s = head, head.next
        while s:
            if s.next and s.val == s.next.val:
                # 还要继续往后找，找到最后一个相等的节点为止
                while s.next and s.val == s.next.val:
                    s = s.next
                f.next = s.next
                s = s.next
            else:
                f = f.next
                s = s.next
        
        return head.next