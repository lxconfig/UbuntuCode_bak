"""
    Cassidy和Eleanore是一对好朋友，她们经常会一起玩游戏。某一天她们玩了一个回文游戏。游戏规则是这样的：给出一个仅包含小写字母的字符串S，在每一个人的回合中，
    她们会进行两个操作：

    1. 尝试重新排列这个字符串，如果可以把这个字符串排列成回文字符串，则立即获胜。

    2. 否则，她们必须删掉字符串中的一个字符。

    已知，Cassidy先手，在两个人都采取最佳策略的情况下，谁可以获胜。
2
aba
ab

Cassidy
Eleanore
9%

思路：在字符串中，任意出现的次数为奇数次的字符的个数(记为odd_num)不能大于1，否则不能构成回文串
如： aba，a字符出现的次数是2，b字符出现的次数是1，此时odd_num=1，则肯定是Cassidy获胜
    abbc，a字符出现1次，b字符2次，c字符1次，此时odd_num=2，则肯定不能构成回文串(就一人一次去掉一个字符，直到只有一个字符)，肯定是Eleanore获胜

"""  

def main(s):
    dict_s = {}   # 用来统计字符串中字符出现的次数
    for i in s:
        if i not in dict_s:
            dict_s[i] = 1
        else:
            dict_s[i] += 1
    odd_num = OddNum(dict_s)   # OddNum()用来判断字符出现次数为奇数的次数
    if odd_num & 1 != 0:
        # 奇数时，Cassidy胜利
        print("Cassidy")
    else:
        # 偶数时，Eleanore胜利
        print("Eleanore")


def OddNum(dict_s):
    odd_num = 0
    for i in dict_s.keys():
        if dict_s[i] & 1 == 1:
            # 奇数
            odd_num += 1
    return odd_num


if __name__ == "__main__":
    main("aba")