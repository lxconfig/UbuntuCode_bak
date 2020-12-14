

"""
    给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
    （注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）

    思路：
        B[i] = A[i-1] * A[i+1] ... * A[n-1] 即 除了A[i], 其他所有数字相乘
        那么就可以认为A[i] = 1
        计算时，可以分别A[0] - A[i-1]的乘积，在计算A[i+1] - A[n-1]的乘积
        再相乘就可以得到B[i]的值
"""


class Solution:
    def multiply(self, A):
        # 运行时间：27ms  占用内存：5624k
        if not A:
            return []
        
        B = []
        length = len(A)
        for i in range(length):
            multi_front_part = 1  # 前半部分的乘积
            multi_back_part = 1   # 后半部分的乘积
            for j in range(i):
                # A[i]的前半部分
                multi_front_part *= A[j]
            for k in range(i+1, length):
                multi_back_part *= A[k]
            B.append(multi_front_part * multi_back_part)
        return B


if __name__ == "__main__":
    solution = Solution()

    print(solution.multiply([1,2,3,4]))
        