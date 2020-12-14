

"""
    在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
    返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。
"""


class Solution:
    def numPairsDivisibleBy60(self, time: list) -> int:
        """普通的双循环方法，数据量很大的时候会超时
        """
        if not time:
            return 0
        count = 0
        length = len(time)
        for i in range(length):
            for j in range(i+1, length):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        return count

    def numPairsDivisibleBy60_2(self, time: list) -> int:
        """创建额外数组
            任何数 % 60的余数，其范围一定在[0, 60]之间
            那么就可以创建一个大小为60的额外数组，记录每个余数出现的次数
            两个数的余数相加若是等于60，那么原来的两个数相加肯定%60==0
            特别的，余数0和余数30只有和自身组合才能满足条件

            执行用时 :260ms, 在所有 Python3 提交中击败了92.82%的用户
            内存消耗 :17.4MB, 在所有 Python3 提交中击败了100.00%的用户
        """
        if not time:
            return 0
        tmp = [0] * 60
        for i in time:
            remainder = i % 60
            tmp[remainder] += 1
        count = 0
        for i in range(31):
            if i == 0 or i == 30:
                count += tmp[i] * (tmp[i] - 1) // 2
            else:
                count += tmp[i] * tmp[60 - i]
        return count

    def numPairsDivisibleBy60_3(self, time: list) -> int:
        """字典
        执行用时 :280 ms, 在所有 Python3 提交中击败了65.04%的用户
        内存消耗 :17.1 MB, 在所有 Python3 提交中击败了100.00%的用户
        """
        if not time:
            return 0
        dicts = {i:0 for i in range(60)}
        for i in time:
            remainder = i % 60
            dicts[remainder] += 1
        # print(dicts)
        count = 0
        for i in range(31):
            if i == 0 or i == 30:
                count += dicts.get(i) * (dicts.get(i) - 1) // 2
            else:
                count += dicts.get(i) * dicts.get(60 - i)
        return count
            

if __name__ == "__main__":
    solution = Solution()
    time = [30,20,150,100,40]
    print(solution.numPairsDivisibleBy60_3(time))