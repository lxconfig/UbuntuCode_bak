
"""
    将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
"""


class Solution:
    def StrToInt(self, s):
        # 运行时间：28ms  占用内存：5736k
        if not s:
            return 0
        dicts = {}
        for i in range(0, 10):
            dicts[str(i)] = i
        s = s.strip()
        ret = 0
        tmp = s
        if s[0] == "+" or s[0] == "-":
            tmp = s[1:]
        for i in range(len(tmp)):
            if tmp[i] in dicts.keys():
                ret = ret * 10 + dicts[tmp[i]]
                # ret += dicts[tmp[i]] * 10 ** (len(tmp) - i - 1)
            else:
                return 0
        return 0-ret if s[0] == "-" else ret

    def StrToInt2(self, s):
        # 运行时间：28ms  占用内存：5764k
        if not s:
            return 0
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        s = s.strip()
        ret = 0
        flag = 1
        if s[0] == "+":
            flag = 1
            s = s[1:]
        elif s [0] == "-":
            flag = -1
            s = s[1:]
        if s:
            for i in s:
                if i in nums:
                    ret = ret * 10 + nums.index(i)
                else:
                    return 0
        return ret * flag
            

if __name__ == "__main__":
    solution = Solution()
    s = "+"
    # print(solution.StrToInt(s))
    print(solution.StrToInt2(s))