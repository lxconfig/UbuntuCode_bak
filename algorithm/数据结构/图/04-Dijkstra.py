import heapq
import sys


graph = {
        "a": {"b": 3, "c": 2, "d": 6},
        "b": {"a": 3, "e": 8},
        "c": {"a": 2, "d": 4, "f": 3},
        "d": {"a": 6, "c": 4, "f": 9},
        "e": {"b": 8, "f": 10},
        "f": {"c": 3, "d": 9, "e": 10}
}


def init_distance(graph, start):
    """初始化每个顶点离起始点的距离
    """
    distance = {start: 0}
    for vertex in graph:
        if vertex != start:
            distance[vertex] = sys.maxsize
    return distance


def Dijkstra(graph, start):
    """求最短路径
    """
    pqueue = []
    visited = set()
    path = {start: None}
    distance = init_distance(graph, start)

    heapq.heappush(pqueue, (0, start))

    while pqueue:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        # print(vertex, end=" ")
        visited.add(vertex)
        for vertxin in graph[vertex].keys():
            if vertxin not in visited:
                if dist + graph[vertex][vertxin] < distance[vertxin]:
                    heapq.heappush(pqueue, (dist + graph[vertex][vertxin], vertxin))
                    distance[vertxin] = dist + graph[vertex][vertxin]
                    path[vertxin] = vertex
    return path, distance


if __name__ == "__main__":
    path, distance = Dijkstra(graph, "a")
    print(path)
    print(distance)