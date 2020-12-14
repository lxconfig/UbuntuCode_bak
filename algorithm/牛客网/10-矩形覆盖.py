

"""
    我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
    比如n=3时，2*3的矩形块有3种覆盖方法

    用青蛙跳台阶的方法来思考。摆放小矩形有两种方式，要么1x2的，要么2x1的
    那么就可以认为是 青蛙要么跳一阶，要么跳两阶
    即：f(n) = f(n-1) + f(n-2)  (n > 2)
    更为一般的结论： f(n) = f(n-1) + f(n-m)  (n > m)

    运行时间：40ms
    占用内存：5832k
"""

class Solution:
    def rectCover(self, number):
        # write code here
        if number < 1:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            a, b, ret = 1, 2, 0
            for _ in range(3, number + 1):
                ret = a + b
                a = b
                b = ret
            return ret


if __name__ == "__main__":
    solution = Solution()
    print(solution.rectCover(5))