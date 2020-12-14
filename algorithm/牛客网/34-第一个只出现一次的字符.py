

"""
    在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）
"""
import pysnooper


# @pysnooper.snoop()
class Solution:
    def FirstNotRepeatingChar(self, s):
        # 运行时间：28ms  占用内存：5856k
        slen = len(s)
        if slen == 0:
            return -1
        if slen == 1:
            return 0
        ret = dict()
        for i in s:
            if i not in ret:
                ret[i] = 1
            else:
                ret[i] += 1
        for i in ret.items():
            if i[1] == 1:
                return s.index(i[0])
        return -1
        # for i in range(slen):
        #     if ret[s[i]] == 1:
        #         return i
        # return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.FirstNotRepeatingChar("google"))