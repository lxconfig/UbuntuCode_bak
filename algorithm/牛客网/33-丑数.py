

"""
    把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
    习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

    思路：每一个丑数，再乘以2， 3， 5就能得到之后三个丑数
"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        # 运行时间：28ms  占用内存：5776k
        if index < 7:
            return index
        q2 = q3 = q5 = 0
        ret = [1]
        curindex = 1
        while curindex < index:
            min_value = min(ret[q2] * 2, ret[q3] * 3, ret[q5] * 5)
            ret.append(min_value)
            while ret[q2] * 2 <= min_value:
                q2 += 1
            while ret[q3] * 3 <= min_value:
                q3 += 1
            while ret[q5] * 5 <= min_value:
                q5 += 1
            
            curindex += 1
        return ret[index - 1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.GetUglyNumber_Solution(8))