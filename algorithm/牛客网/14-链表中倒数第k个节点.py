
"""
    输入一个链表，输出该链表中倒数第k个结点。
    以空间换时间
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        '''
        # 运行时间：22ms  占用内存：5856k
        ret = []
        while head:
            ret.insert(0, head.val)  # 写成head才能过
            head = head.next
        if k > len(ret) or k <= 0:
            return 
        return ret[k-1]
        '''
        # 运行时间：30ms  占用内存：5704k
        # 就像一把尺子，当把尺子的右端移动到链表末尾，尺子的左端就对应着那个值，即倒数的第k个节点
        temp = head
        if head == None or k <= 0:
            return
        while k > 1:
            if temp.next:
                # 先让temp走k步
                temp = temp.next
                k -= 1
            else:
                # temp已经移到链表外面，说明k不合法
                return
        # 之后temp和head一起走，直到temp走到末尾
        while temp.next:
            head = head.next
            temp = temp.next
        
        return head.val



if __name__ == "__main__":
    solution = Solution()

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    print(solution.FindKthToTail(a, 3))