

"""
    给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

    思路：
        双指针法
        快指针先走两步，慢指针走一步
        当两个指针又相遇了，此时指向的节点可能是环的入口节点
        再次让慢指针回到链表头，然后和快指针一起走，再次相遇时，就是环的入口节点
        否则，快指针不存在时，表示没有环

    或：
        先让快指针走n步，n=链表的长度
        之后再让快指针和慢指针一起走，直到相遇，此时就是环的入口节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # 运行时间：22ms  占用内存：5864k
        if not pHead:
            return None
        fast = slow = pHead
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        slow = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast.val


if __name__ == "__main__":
    solution = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    a.next= b
    b.next = c
    c.next = d
    d.next = e
    e.next = c
    # f.next = d
    print(solution.EntryNodeOfLoop(a))