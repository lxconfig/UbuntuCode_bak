

"""
    输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
    例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""


class Solution:
    def PrintMinNumber(self, numbers):
        # 运行时间：23ms  占用内存：5672k
        n = len(numbers)
        if n == 0:
            return 0
        if n == 1:
            return numbers[0]
        
        # 排序，但不是按照一般的规则排序，而是：
        # ab > ba, 则 a > b
        # ab < ba, 则 a < b
        # ab = ab, 则 a = b
        # 如: a = 3  b = 32, 虽然 3 < 32
        # 但 332 > 323, 所以 3 > 32
        tmp = [str(i) for i in numbers]
        for i in range(1, n):
            for j in range(i, 0, -1):
                if tmp[j] + tmp[j-1] < tmp[j-1] + tmp[j]:
                    tmp[j], tmp[j-1] = tmp[j-1], tmp[j]
                else:
                    break
        return "".join(tmp)

if __name__ == "__main__":
    solution = Solution()
    numbers = [3, 32, 321]
    print(solution.PrintMinNumber(numbers))
