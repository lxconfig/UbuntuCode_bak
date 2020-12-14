
"""
    你有一堆绳子，每个绳子的长度保存在数组中，你需要把这些绳子连接成一根绳子，但连接每两个绳子都会花费一些成本
    假设成本和绳子长度一样长，求连接全部绳子的最小成本是多少？

    思路：用最小堆，每次从堆中取出当前最小的两根绳子，计算连接后的长度及成本，并放回堆中，然后继续取
"""


import heapq


def ropeCost(array):
    heapq.heapify(array)  # 构成最小堆
    cost = 0
    while array:
        shortest = heapq.heappop(array)
        shorter = heapq.heappop(array)
        new_rope = shortest + shorter
        cost += new_rope
        if not array:
            # 当最后两根绳子被取出时，结束循环，不用在放回堆中
            break
        heapq.heappush(array, new_rope)
    return cost


if __name__ == "__main__":
    array = [4, 3, 2, 6]
    print(ropeCost(array))