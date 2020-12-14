

def main():
    """
        找到一些字符串的公共子串
    """
    # 可以用zip()来做  
    # zip()将两个列表，打包成[(), ()].如 a = [1,2] b = [3, 4] zip(a,b) = [(1, 3), (2, 4)]
    # zip(*d)表示反操作，将[(1,3), (2,4)]解压成  [(1, 2), (3, 4)]
    # 若d=[1, 2] zip(*d) = [(1, ), (2, )]
    a = ['flower','flow','flight']
    result = ""
    for i in zip(*a):
        if len(set(i)) == 1:
            result += i[0]
    print(result)


if __name__ == "__main__":
    main()