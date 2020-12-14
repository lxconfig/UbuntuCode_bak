"""
    初始你只有一次抽卡机会。每次抽卡浪费一次抽卡机会，获得一张卡片。这张卡片上有两个数字，第一个数字代表你能获得的钱，第二个数字代表你能获得的额外抽卡次数。
    额外的抽卡次数是可以累计的。

现在，你知道了卡片的数量，所有的卡片上的数字，以及所有卡片的顺序。你只需要安排一种抽卡顺序，使得你能获得钱数最多

输入：
5
0 2
1 1
1 0
1 0
2 0
输出：
4
18%
"""


# while True:
#     n = int(input())
#     ab = []
#     # m, k = [], []
#     for i in range(0, n):
#         ab.append(list(map(int, input().split(" "))))
#     # print(ab)
#     temp = []
#     money = 0
#     c = 1
#     for i in ab:
#         if (i[1] > 0):
#             money += i[0]
#             c += i[1] - 1
#         else:
#             temp.append(i[0])
#     temp.sort()
#     money += sum(temp[len(temp)-c:])
#     print(money)

    # c = 1  # 抽奖次数
    # money = 0  # 钱数
    # params = [j for i in ab for j in i]
    # for i in range(0, len(params)):
    #     if i % 2 == 0:
    #         m.append(params[i])
    #     else:
    #         k.append(params[i])
    # for i in range(len(m)-1,0,-1):
    #     if k[i] != 0:
    #         c = c + k[i] - 1
    #         money += m[i]
    # print(c)

    # for i in range(0, c):
    #     money = money + m[-1] + m[-2]
    #     c -= 2
    # print(c)
    # print(money, end=" ")    

def main():
    card = [[0,2],[1,1],[1,0],[1,0],[2,0]]
    point = 0  # 钱数
    count = 1  # 抽奖次数
    ps = []
    for i in card:
        print(i,i[1])
        if (i[1] > 0):
            print(i)
            point += i[0]
            count += i[1]-1
        # card.remove(i)
        else:
            ps.append(i[0])
    ps.sort()
    point += sum(ps[len(ps)-count:])
    print(point)


if __name__ == "__main__":
    main()