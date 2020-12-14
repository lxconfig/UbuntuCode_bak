
'''
    保留上一次的计算结果，以供下一次计算去使用
    
    运行时间：21ms
    占用内存：5856k
    时间复杂度：O(n)
'''


class Solution:
    def Fibonacci(self, n):
        a, b, ret = 0, 1, 0
        if n == 0:
            return 0
        while n > 0:
            # ret = b
            a, b = b, a+b
            ret = a
            # print(a, b)
            n = n - 1
        return ret


if __name__ == "__main__":
    solution = Solution()
    print(solution.Fibonacci(3))