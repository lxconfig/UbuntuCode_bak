

"""
"""
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue, visited, step, wordList = [], set(), 1, set(wordList)
        queue.append(beginWord)
        visited.add(beginWord)
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                # 遍历每一位的所有可能(每一位都有26种可能a-z)
                node_len = len(node)
                node_list = [i for i in node]
                for i in range(node_len):
                    # 记录原来的单词的第i个字符
                    # 因为如果改变的第i个字符不能满足条件，需要还原回去
                    # 不然会影响下一位的遍历
                    original_word = node_list[i]
                    for j in range(26):
                        # 从a-z依次枚举判断
                        # ord()：字符 -> ASCII码
                        # chr(): ASCII码 -> 字符
                        node_list[i] = chr(ord("a") + j)
                        # 就是改变第i个字符后的word
                        next_word = "".join(node_list)
                        # *** 线性判断, 会超时 ***
                        # 把wordList改成集合就可以了
                        if next_word in wordList:
                            if next_word == endWord:
                                # +1也就是要把next_word也算上
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                visited.add(next_word)
                        node_list[i] = original_word
            step += 1
        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution = Solution()
    res = solution.ladderLength(beginWord, endWord, wordList)
    print(res)