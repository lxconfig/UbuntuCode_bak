

"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s: return [[]]
        size, res, path = len(s), [], []
        def backtracking(s, start, res, path):
            """
            s: 原字符串
            start: 开始搜索的起始位置
            res: 最终的结果列表
            path: 记录路径（也就是记录回文串）
            """
            # 终止条件，说明已经判断完字符s
            if start == size:
                res.append(path[:])
                return
            for i in range(start, size):
                if not is_Palindrome(s, start, i):
                    # 说明s[start...i]不是回文串，也就不用继续判断
                    continue
                # 否则说明是回文串，可以加入路径path
                path.append(s[start: i + 1])
                # 回溯，判断下一个，本次判断的是s[start...i]，那么下次就从i+1开始
                backtracking(s, i + 1, res, path)
                # 撤销选择
                path.pop()

        def is_Palindrome(s, left, right):
            """判断s中某个范围的字符串是否是回文串
            s: 原字符串
            left: 要判断的子字符串左边界
            right: 要判断的子字符串右边界
            """
            while left < right:
                if s[left] != s[right]: return False
                left, right = left + 1, right - 1
            return True
        
        backtracking(s, 0, res, path)
        return res