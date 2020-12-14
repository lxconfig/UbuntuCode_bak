# 不带参数不带返回值的装饰器
def common_decorate(func):
    def wrapper():
        print("---wrapper---")
        func()
    return wrapper

@common_decorate  # 等价于 no_para_return = common_decorate(no_para_return)
def no_para_return():
    print("---no_para_return---")


# 带参数不带返回值的装饰器
def para_decorate(func):
    def wrapper(num, sp):
        print("---wrapper---")
        func(num, sp)
    return wrapper

@para_decorate
def para_no_return(num, sp):
    print("para_no_return %s,%s" % (num, sp))


# 不带参数有返回值的装饰器
def return_decorate(func):
    def wrapper():
        print("---wrapper---")
        return func()
    return wrapper

@return_decorate
def no_para_have_return():
    print("no_para_have_return")
    return "ok"


# 带参数有返回值的装饰器
def decorate(func):
    def wrapper(*args, **kwargs):
        print("--wrapper--")
        return func(*args, **kwargs)
    return wrapper

@decorate
def para_return(*args, **kwargs):
    print("para_return")
    # print(*args, **kwargs) 表示拆包，等价于 print(100,200,t=1,r=2)
    # 但是这样会把t，r认为是print函数的参数，所以会报错
    print(args, kwargs)  # 原封不动作为 元组和字典 输出
    return "ok"


# 有参数的装饰器
def sets(num):
    def set_func(func):
        def wrapper(*args, **kwargs):
            print("---wrapper--- %s" % num)
            return func(*args, **kwargs)
        return wrapper
    return set_func


# 先调用sets函数，并将1作为参数
# 将sets函数的返回值作为装饰器
@sets(1)
def have_para_decorate(*args, **kwargs):
    print("have_para_decorate")
    print(args, kwargs)
    return "ok"


if __name__ == "__main__":
    # no_para_return()

    # para_no_return(100, "abc")

    # print(no_para_have_return())

    # print(para_return(100, 200, t=1, r=2))

    print(have_para_decorate(100, 3232, hf="sg", sd="1GB"))