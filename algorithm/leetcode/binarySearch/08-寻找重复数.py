
from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        hashMap = dict()
        for i in range(len(nums)):
            if hashMap.get(nums[i]) != None:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1
        for key, value in hashMap.items():
            if value > 1:
                return key


if __name__ == "__main__":
    s = Solution()
    nums = [1,3,4,2,2]
    print(s.findDuplicate(nums))