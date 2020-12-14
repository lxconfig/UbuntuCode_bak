

"""
    请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
    当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

    思路：哈希表（字典）
"""


class Solution:
    # 运行时间：30ms  占用内存：5868k
    def __init__(self):
        self.s = ""
    
    def FirstAppearingOnce(self):
        # dicts = {}
        # for i in self.s:
        #     if i not in dicts:
        #         dicts[i] = 1
        #     else:
        #         dicts[i] += 1

        # for i in self.s:
        #     if dicts[i] == 1:
        #         return i
        # return "#"
        tmp = list(filter(lambda i: self.s.count(i) == 1, self.s))
        return tmp[0] if tmp else "#"

    def Insert(self, char):
        self.s += char


if __name__ == "__main__":
    solution = Solution()
    solution.Insert("google")
    print(solution.FirstAppearingOnce())