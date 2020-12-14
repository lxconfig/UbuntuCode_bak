

"""
    请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
    但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

    思路：
        1. 包含+/-号
            1.1 +号要么不出现，要么只能出现在第一个位置
            1.2 -号要么不出现，要么出现在一个位置，或者e的后面
        2. 除了E/e之外，不能出现其他任何字母
        3. 小数点只能出现一次，并且E/e之后不能有小数点
"""

import re


class Solution:
    # s字符串
    def isNumeric(self, s):
        # 运行时间：31ms  占用内存：5752k
        if not s:
            return False
        legal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # +/-号，小数点，E/e的是否出现的标记
        sign, dots, hasE = False, False, False
        length = len(s)
        for i in range(length):
            if s[i] == "e" or s[i] == "E":
                if i == length - 1:
                    return False      # E/e后面没有数字了
                if hasE:
                    return False      # 不能重复出现E/e
                hasE = True
            elif s[i] == "+" or s[i] == "-":
                if i > 0 and s[i-1] != "E" and s[i-1] != "e" and not sign:
                    return False      # 第一次出现+/-号，若不是在第一个位置出现，且前面不是E/e，就返回False
                if s[i-1] != "E" and s[i-1] != "e" and sign:
                    return False      # 第二次出现+/-号，前面不是E/e，返回False
                sign = True
            elif s[i] == ".":
                if hasE or dots:
                    return False      # 前面已经又E/e，就不能有小数点
                dots = True
            elif s[i] not in legal:
                return False
        return True
            
    def isNumeric2(self, s):
        """正则表达式解法
        """
        # 运行时间：31ms  占用内存：5852k
        pattern = r'^[\+-]?[0-9]*(\.[0-9]*)?([Ee][\+-]?[0-9]+)?$'
        return re.match(pattern, s)

if __name__ == "__main__":
    solution = Solution()
    s = "12e"
    print(solution.isNumeric2(s))