

"""
    牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
    例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
"""


class Solution:
    def ReverseSentence(self, s):
        # 运行时间：30ms  占用内存：5624k
        if not s:
            return ""
        # s = "  "  只有空格没有数据
        if s.strip() != "":
            return " ".join(s.split()[::-1])
        else:
            return s

    def ReverseSentence2(self, s):
        if not s:
            return ""
        if s.strip() != "":
            stack = [i for i in s.split()]
            return " ".join(stack[::-1])
        return s


if __name__ == "__main__":
    solution = Solution()
    s = "I am a student."
    print(solution.ReverseSentence2(s))