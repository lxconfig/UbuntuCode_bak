
"""
    python3.8新特性之一： 海象运算符
    1. 使用方式
        变量 := 函数
    2. 作用
        用一句话概括海象运算符: 在一些表达式中，能够将计算结果赋值给变量，然后该变量可以在代码块中使用
        减少了中间变量的赋值操作，以及一些函数的重复调用
"""


def main():
    """海象运算符基本使用
    """
    if b := len("sss") > 0:
        # b = True，并不是len("sss")的长度
        print(b)
        print("yes")
    else:
        print("no")

# 等价于下面的函数
def test():
    b = len("sss")
    if b > 0:
        print("yes")
    else:
        print("no")






if __name__ == "__main__":
    main()