
"""
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        """双指针进行比较
        1. 若left和right指向的都不是元音字母，则一起移动
        2. 若left是，right不是，则移动right，反之移动left
        3. 若left和right都是元音字母，且不相同，则交换字母，移动指针，否则不用交换，直接移动指针（相同的字母没必要交换）
        循环条件就是left < right
        """
        if not s: return ""
        # 把字符串转为列表，方便交换，用字典会稍微快一点
        arr, alphabet = [i for i in s], {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] in alphabet and arr[right] in alphabet:
                # 都是元音字母，且不等则交换
                if arr[left] != arr[right]:
                    arr[left], arr[right] = arr[right], arr[left]
                    left, right = left + 1, right - 1
                else:
                    # 都是元音字母，但相等，则不交换
                    left, right = left + 1, right - 1
            # 这样写会增加更多循环次数
            # elif arr[right] not in alphabet:
            #     right -= 1
            # elif arr[left] not in alphabet:
            #     left += 1
            # else:
            #     # 都不是元音字母
            #     left, right = left + 1, right - 1
            if arr[right] not in alphabet:
                right -= 1
            if arr[left] not in alphabet:
                left += 1
        return "".join(arr)



if __name__ == "__main__":
    ss = Solution()
    s = "Live on evasions? No, I save no evil."
    n = s.strip("")
    print(n)
    # print(ss.reverseVowels(s))
