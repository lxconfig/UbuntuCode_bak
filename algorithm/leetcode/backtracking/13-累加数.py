
"""
"""

from typing import List


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        size = len(num)
        # 长度小于3肯定不能构成累加序列
        if size < 3: return False
        # 只要根据两个数，就能得到第三个数
        # 枚举两个数
        for i in range(size):
            # 剔除掉一些不合法的情况，比如开头数字是0的情况，01，02之类的
            num1 = num[: i + 1]
            if num1.startswith('0') and len(num1) > 1:
                return False
            for j in range(i + 1, size):
                num2 = num[i + 1: j + 1]
                if num2.startswith('0') and len(num2) > 1:
                    break
                num3 = num[j + 1: ]
                if self.isValid(num1, num2, num3) and num3:
                    return True
        return False

    def isValid(self, num1, num2, num3):
        while num3:
            pre_sum = str(int(num1) + int(num2))
            if num3.startswith(pre_sum):
                num1 = num2
                num2 = pre_sum
                num3 = num3[len(pre_sum): ]
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    num = "112358"
    print(s.isAdditiveNumber(num))