

"""
    给你一个整数数组 arr 和两个整数 k 和 threshold 。请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。
    例：
        输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
        输出：3
"""


class Solution:
    def numOfSubarrays_1(self, arr: list, k: int, threshold: int) -> int:
        """滑动窗口
        法1：仅使用两个指针滑动时：
            还是属于暴力法，一个一个子数组遍历
            只适合小数据，大数据超时
            时间消耗在sum()的计算中
        """
        if not arr or k == 0:
            return 0
        count = 0
        low, high = 0, k - 1
        while high <= len(arr) - 1:
            if sum(arr[low: high+1]) / k >= threshold:
                count += 1
                low += 1
                high += 1
            else:
                low += 1
                high += 1
        return count

    def numOfSubarrays(self, arr: list, k: int, threshold: int) -> int:
        """滑动窗口
        法1：仅使用两个指针滑动时：
            还是属于暴力法，一个一个子数组遍历
            只适合小数据，大数据超时
        法2：法1的问题在于每次循环都调用sum()计算当前子数组的和， 数据量很大时会非常慢
            改进：
                把前一次子数组的和s记录下来，下一个子数组的和只需要计算 【s-移走的元素+新进入的元素】 即可
                同时，比较均值也可以先计算出一个总值，比较大小即可，不用计算除法
        """
        if not arr or k == 0:
            return 0
        count = sum_of_k = 0
        target = k * threshold
        for i in range(len(arr) - k + 1):
            if i == 0:
                sum_of_k = sum(arr[:k])
            else:
                sum_of_k = sum_of_k - arr[i - 1] + arr[i + k - 1]
            if sum_of_k >= target:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    arr = [2,2,2,2,5,5,5,8]
    print(s.numOfSubarrays(arr, 3, 4))