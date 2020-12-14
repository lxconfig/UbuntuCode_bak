

"""
    在迷宫问题2的基础上，求起点到终点的最短距离
    
    思路：考虑Dijstra算法(也就是BFS算法的思想)
"""
import heapq


def shortestDistance(matrix, start, end):
    def neighbors(matrix, node):
        destination = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dest in destination:
            curNode, dist = list(node), 0
            while 0 <= curNode[0] + dest[0] < len(matrix) and 0 <= curNode[1] +  dest[1] < len(matrix[0]) and matrix[curNode[0]+dest[0]][curNode[1]+dest[1]] == 0:
                curNode[0] += dest[0]
                curNode[1] += dest[1]
                dist += 1
            yield dist, tuple(curNode)

    pqueue = [(0, start)]
    visited = set()
    while pqueue:
        dist, node = heapq.heappop(pqueue)
        if node in visited: continue
        if node == end:
            # 找到了终点，返回此时的距离dist
            return dist
        visited.add(node)
        for neighbor_dist, neighbor in neighbors(matrix, node):
            heapq.heappush(pqueue, (dist + neighbor_dist, neighbor))
    return -1


if __name__ == "__main__":
    matrix = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    print(shortestDistance(matrix, start, end))