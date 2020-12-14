

"""
    求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

    思路：
        用递归来模拟循环
        用短路规则来结束递归

    python 中 and的特性：
        a and b                                        a or b
        当 a = False 时，返回a                          当 a = False 时，返回b
        当 a = True  时，返回b                          当 a = True  时，返回a
    如:  
        0 and 1 = 0                                    0 or 1 = 1
        0 and 0 = 0                                    0 or 0 = 0
        1 and 0 = 0                                    1 or 0 = 1
        1 and 2 = 2                                    1 or 2 = 1
"""


class Solution:
    def Sum_Solution(self, n):
        # 运行时间：22ms  占用内存：5724k
        # ret = n
        # tmp = ret and self.Sum_Solution(n - 1)
        # ret += tmp
        # return ret
        return n and (n + self.Sum_Solution(n - 1))
    
    def Sum_Solution2(self, n):
        # 运行时间：22ms  占用内存：5860k
        return (pow(n, 2) + n) >> 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.Sum_Solution(3))