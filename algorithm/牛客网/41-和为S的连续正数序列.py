

"""
   小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
   但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
   没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
   现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck! 
"""
import pysnooper


class Solution:
    def FindContinuousSequence(self, tsum):
        # 运行时间：23ms  占用内存：5748k
        # 暴力法，一个一个计算
        if tsum == 0:
            return [[0]]
        sequence = []
        ret = []
        for i in range(1, tsum):
            sequence.append(i)
            for j in range(i+1, tsum):
                sequence.append(j)
                if sum(sequence) == tsum:
                    oneSequence = []
                    for num in sequence:
                        oneSequence.append(num)
                    ret.append(oneSequence)
                # 当前和已经大于tsum时，说明sequence中的数字不可能和为tsum，则清空
                if sum(sequence) > tsum:
                    sequence = []
                    break
        return ret
    

    # @pysnooper.snoop()
    def FindContinuousSequence2(self, tsum):
        """双指针法
        或 滑动窗口法
        借助公式: Sn = (a0 + an) * n // 2
        """
        # 运行时间：23ms  占用内存：5728k
        if tsum == 0:
            return [[0]]
        # sequences = [i for i in range(1, tsum)]
        ret = []
        low, high = 1, 2
        while low < high:
            if (low + high) * (high - low + 1) >> 1 == tsum:
                ret.append([i for i in range(low, high+1)])
                low += 1
            elif (low + high) * (high - low + 1) >> 1 < tsum:
                high += 1
            else:
                low += 1
        return ret



if __name__ == "__main__":
    solution = Solution()
    # print(solution.FindContinuousSequence(4))
    print(solution.FindContinuousSequence2(100))