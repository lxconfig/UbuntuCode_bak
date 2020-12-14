

"""
    LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,
    如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大/小王可以看成任何数字,
    并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 
    现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。

    思路:
        首先判断有没有大小王，即有没有0
        当没有0时：计算相邻两个值之间的差值，差值不为1，则肯定不是顺子，否则是顺子
        当有0时，把数组里的0先剔除掉，然后计算剩余数字的差值gap，如果gap > 大小王的个数，则肯定不是顺子
        此外，有0时，还要判断数组中是否有对子

"""


class Solution:
    def IsContinuous(self, numbers):
        # 运行时间：24ms   占用内存：5860k
        # numbers是数组，即抽的5张牌
        if not numbers:
            return False
        numbers.sort()
        zeros = numbers.count(0)
        for _ in range(zeros):
            numbers.remove(0)
        # 大小王比其他数字还多，仅针对1个数字，4个大小王
        # 当有3个大小王，2个数字时，还是要判断
        if len(numbers)  + 1 < zeros:
            return True
        if zeros == 0:
            # 没有大小王,计算相邻两张牌的差值是否为1
            for i in range(1, len(numbers)):
                if numbers[i] - numbers[i-1] != 1:
                    return False
            return True
        else:
            # 有大小王，计算总的差值，判断是否能被大小王的数量补齐
            gap = 0
            for i in range(1, len(numbers)):
                # 有对子
                if numbers[i] == numbers[i-1]:
                    return False
                gap += numbers[i] - numbers[i-1] - 1
            if gap > zeros:
                return False
            else:
                return True


if __name__ == "__main__":
    solution = Solution()
    numbers = [0,3,1,6,4]
    print(solution.IsContinuous(numbers))