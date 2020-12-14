

"""
    给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        """双指针法
            先让快指针走两步，然后慢指针走一步
            当两个指针再次相遇时，指向的元素可能是入口元素，也可能不是
            可以再让慢指针回到头指针位置，然后和快指针同步走
            再次相遇的位置，就是入口节点
        """
        if not pHead:
            return None
        fast = slow = pHead
        if not fast or not fast.next:
            return None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        slow = pHead
        while slow != fast:
            fast = fast.next
            slow = slow.next
        
        return slow


if __name__ == "__main__":
    s = Solution()
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a3
    print(s.EntryNodeOfLoop(a1))