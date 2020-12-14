

"""
    一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # 运行时间：22ms  占用内存：5732k
        # 先异或，找出两个只出现一次数字的异或结果
        tmp = l = m = 0
        if not array:
            return []
        for i in array:
            tmp ^= i
        # 根据异或结果的二进制，找到其最低位的1的位置，由此位置把数组拆分开
        index = self.FindFirst1(tmp)
        for i in array:
            if self.isBit1(i, index):
                l ^= i
            else:
                m ^= i
        return [l, m]
    
    def FindFirst1(self, num):
        """找到二进制数中最低位的1"""
        index = 0
        while num & 1 == 0:
            # 如果是偶数，说明还没有找到最低位的1
            # 如：0010  右移一次后是：001  所以index=1
            num >>= 1
            index += 1
        return index

    def isBit1(self, num, index):
        """检查num二进制中index位置是否为1"""
        # 因为要检查的是index位，所以index后面的位数都不用看，右移直接去掉
        # 之前是index位，右移后，肯定是最低位，如果为1，肯定是奇数，如果为0，肯定是偶数
        return (num >> index) & 1 == 0


if __name__ == "__main__":
    solution = Solution()
    array = [1, 2, 2, 3, 4, 4]
    print(solution.FindNumsAppearOnce(array))

