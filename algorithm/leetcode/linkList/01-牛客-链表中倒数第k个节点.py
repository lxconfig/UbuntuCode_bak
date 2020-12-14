

"""
    输入一个链表，输出该链表中倒数第k个结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        """双指针法
        先让fast指针走k步，再和slow指针一起走，直到fast指针越界
        """
        if not head or k == 0:
            return None
        fast = slow = head

        # fast先走k步
        for _ in range(k):
            if fast:
                fast = fast.next
            else:
                return None   # k太大
        while fast:
            fast, slow = fast.next, slow.next
        
        return slow.val

    def FindKthToTail_2(self, head, k):
        """遍历法
        一个一个遍历,保存到列表中
        """
        if not head or k <= 0:
            return None
        ret = []
        tmp = head
        while tmp:
            ret.insert(0, tmp)
            tmp = tmp.next
        return ret[k-1] if len(ret) >= k else None

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
    print(s.FindKthToTail_2(a1, 3))