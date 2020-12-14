
"""
    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
    输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
    例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
    NOTE：给出的所有元素都大于0，若数组大小为0，请返回0

    运行时间：853ms
    占用内存：5856k
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # if len(rotateArray) == 0:
        #     return 0

        # ret = rotateArray[0]
        # if len(rotateArray) == 1:
        #     return ret
        
        # for i in range(1, len(rotateArray)):
        #     if rotateArray[i] < ret:
        #         ret = rotateArray[i]
        #         break
        # return ret

        # 二分法  运行时间：761ms  占用内存：5756k
        n = len(rotateArray)
        if n == 0:
            return 0
        if n == 1:
            return rotateArray[0]
        left, right = 0, n-1
        while left < right:
            if rotateArray[left] < rotateArray[right]:
                # 可能全部旋转得情况  [1,2,3,4,5]  旋转后  [1,2,3,4,5]
                return rotateArray[left]
            mid = (left + right) // 2
            if rotateArray[mid] > rotateArray[left]:
                left = mid + 1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                # 数组中有重复值得情况
                left += 1
        return rotateArray[right]




if __name__ == "__main__":
    solution = Solution()
    array = [1,0,1,1,1]
    print(solution.minNumberInRotateArray(array))