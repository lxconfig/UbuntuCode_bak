

"""

    假设n = 7543 [x] 29
    如果要让百位的x为1
        (1) 百位就是1时，前面的四位数的取值范围是：0000-7542=7543种可能(都是小于n的可能),后面两位数的范围是：00-99=100种可能(可以随便取，前面四位已经保证整个数是小于n的)
            总次数就是 7543 * 100
        
        (2.1) 前面四位就取7543，若百位的x > 1, 如n = 7543 [6] 29, 那么就可以在比n小的数中取到百位是1的数字，后两位还是可以随便取00-99=100种可能
            总次数就是 1 * 100
        
        (2.2) 前面四位还是7543，但百位的x = 1, 如n = 7543 [1] 29, 那么后两位就不能随便取值(因为要小于n), 后两位的取值范围就是 00-29=30种可能
            总次数就是 1 * 30
        
        (2.3) 前面四位还是7543，但百位的x = 0，如n = 7543 [0] 29，那么不可能取到百位是1的情况(因为肯定比n大了)
"""



class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # 运行时间：31ms  占用内存：5860k
        m = len(str(n))  # 数字的长度
        count = 0
        for i in range(1, m+1):
            high = n // 10 ** i                       # 找到当前位之前的位数
            mid = n % 10 ** i // 10 ** (i - 1)        # 找当前位
            low = n % 10 ** (i - 1)                   # 找当前位后面的位数
            # 第(1)个情况
            count += high * (10 ** (i - 1))

            if mid > 1:
                # 第(2.1)个情况
                count += 10 ** (i - 1)
            elif mid == 1:
                # 第(2.2)个情况
                count += (low + 1)
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.NumberOf1Between1AndN_Solution(99))