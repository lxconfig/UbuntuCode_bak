

"""
    给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
    请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        if not nums1:
            length = len(nums2)
            mid = length // 2
            if length & 1 == 0:
                return (nums2[mid] + nums2[mid-1]) / 2.0
            else:
                return nums2[mid] / 1.0
        elif not nums2:
            length = len(nums1)
            mid = length // 2
            if length & 1 == 0:
                return (nums1[mid] + nums1[mid-1]) / 2.0
            else:
                return nums1[mid] / 1.0
        else:
            length1, length2 = len(nums1), len(nums2)
            length = length1 + length2
            mid = length // 2
            i, j, tmp = 0, 0, []
            while i < length1 and j < length2:
                if nums1[i] <= nums2[j]:
                    tmp.append(nums1[i])
                    i += 1
                else:
                    tmp.append(nums2[j])
                    j += 1
            if i < length1:
                tmp.extend(nums1[i:])
            if j < length2:
                tmp.extend(nums2[j:])
            if length & 1 == 0:
                return (tmp[mid] + tmp[mid-1]) / 2.0
            else:
                return tmp[mid] / 1.0


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 3]
    nums2 = [2, 4]
    print(s.findMedianSortedArrays(nums1, nums2))            