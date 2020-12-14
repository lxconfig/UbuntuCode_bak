
"""
    将一个数a的二进制的第n位设置成1，如果本来就是1则不变

    思路：就是要把 0 -> 1, 或运算|刚好能把0转为1，而且对1不受影响
    假设a的二进制是 0010 0[0]10，把第2位改为1
    就是构造一个二进制数： 0000 0[1]00 | a 即可
    可以通过左移n位，来构造这个二进制数

    同理可以得到相反的操作，即 把第n位设置成0  与操作
"""


def set_bit(a, n):
    # 0 -> 1
    return a | (1 << n)
    # return a + 2 ** n


def clear_bit(a, n):
    # 1 -> 0
    return a & (~(1 << n))
    # return a - 2 ** n


def Toggle_bit(a, n):
    """翻转第n位
    1 -> 0    0 -> 1
    """
    return a ^ (1 << n)


if __name__ == "__main__":
    a = 125
    n = 2
    print(bin(a))
    # b = set_bit(a, n)
    # c = clear_bit(a, n)
    # print(a, b, c)
    # print(bin(b))
    # print(bin(c))
    d = Toggle_bit(a, n)
    print(a, d)
    print(bin(d))