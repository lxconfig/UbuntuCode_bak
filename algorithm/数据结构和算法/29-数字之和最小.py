

"""
    给定一个m，表示位数，再给定一个s，表示m位数之和。求满足这个条件的最小数
    例子：m=2，s=9  output=18
    给一个两位数，其个位和十位加起来等于9，求最小的满足条件的数字
    满足条件的有：18，81，36，63，27，72，90，45，54

    思路：不管和s是多少，除去最低位，起码要留1给最高位
    可以先把s-1留给最高位，剩下给低位分
    从最低位开始，如果剩余的s<9，就全部给最低位
    如果剩余的s>9,就只给9给最低位
"""


def findSmallest(s, m):
    if s == 0:
        if m == 0:
            return 0
        else:
            return None
    
    if s > m * 9:
        return None
    
    res = [0 for i in range(m + 1)]
    s -= 1
    for i in range(m-1, 0, -1):
        if s > 9:
            res[i] = 9
            s -= 9
        else:
            res[i] = s
            s = 0
    res[0] = s + 1
    
    return "".join(map(str, res[:m]))


if __name__ == "__main__":
    print(findSmallest(9, 4))