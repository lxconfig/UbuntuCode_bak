
"""
    随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,
    继续0...m-1报数....这样下去....直到剩下最后一个小朋友。
    请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1).如果没有小朋友，请返回-1

    约瑟夫环问题
        f(n, m) = [f(n-1, m) + m] % n    n > 1
        f(n, m) = 0                      n = 1
"""


class Solution:
    def LastRemaining_Solution(self, n, m):
        # 运行时间：26ms  占用内存：5860k
        if n == 0:
            return -1
        ret = 0
        for i in range(2, n+1):
            ret = (ret + m) % i
        return ret
    
    def LastRemaining_Solution2(self, n, m):
        if n == 0:
            return -1
        if n == 1:
            return 0
        children = [i for i in range(n)]
        index = 0
        while len(children) > 1:
            remove_index = (index + m - 1) % n
            children.pop(remove_index)
            n -= 1
            index = remove_index
        return children[0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.LastRemaining_Solution(10, 3))