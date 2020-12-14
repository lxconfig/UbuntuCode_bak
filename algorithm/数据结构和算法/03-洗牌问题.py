import random


def main(a):
    """
        将数组里的数字打乱
    """
    # a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(0, len(a)):
        randomi = i + random.randint(0, (len(a)-i-1))  # 剔除掉上一次替换过的位置
        a[i], a[randomi] = a[randomi], a[i]


def test_shuffle():
    result = [[0 for i in range(10)] for j in range(10)]
    for i in range(1000):
        a = [i for i in range(0, 10)]
        main(a)
        for j in range(10):
            result[a[j]][j] += 1
    print("\n".join(["".join(["{:6}".format(item) for item in row]) for row in result]))


if __name__ == "__main__":
    test_shuffle()