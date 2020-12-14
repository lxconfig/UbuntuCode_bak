

"""
    汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
    例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
"""


class Solution:
    def LeftRotateString(self, s, n):
        # 运行时间：27ms  占用内存：5724k
        if not s:
            return ""
        sLen = len(s)
        if sLen == n or sLen == 1:
            return s
        
        tmp = [i for i in s]
        if sLen < n:
            tmp.append(tmp.pop(0))
            return "".join(tmp)
        while n:
            tmp.append(tmp.pop(0))
            n -= 1
        return "".join(tmp)

    def LeftRotateString2(self, s, n):
        # 运行时间：23ms  占用内存：5712k
        if not s:
            return ""
        # 获取真正要左移的次数n
        # n如果很大，大于了s的长度，就只要左移n % len(s)次
        n = n % len(s)
        return s[n:] + s[:n]


if __name__ == "__main__":
    solution = Solution()
    s = "ab"
    print(solution.LeftRotateString(s, 3))
    print(solution.LeftRotateString2(s, 3))