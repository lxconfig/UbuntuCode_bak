
class Vertex:
    """顶点类"""
    def __init__(self, node):
        self.id = node
        self.visited = False
    
    def addNeighbor(self, neighbor, G):
        """添加一个邻居节点"""
        G.addEdge(self.id, neighbor)
    
    def getConnections(self, G):
        return G.adjMatrix[self.id]
    
    def getVertexID(self):
        """获取顶点的id(标识)"""
        return self.id

    def setVertexID(self, id):
        """设置顶点的id(标识)"""
        self.id = id
    
    def setVisited(self):
        self.visited = True
    
    def __str__(self):
        return str(self.id)


class Graph:
    def __init__(self, numVertices=10, directed=False):
        """
            numVertices=10: 顶点个数最大为10个
            directed=False: 是否为有向图，默认为无向图
        """
        self.adjMatrix = [[None] * numVertices for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []   # 保存着所有的顶点(是Vertex类的对象)
        self.directed = directed
        for i in range(numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)
    
    def addVertex(self, vtx, id):
        """添加顶点
            必须在 0 <= v < numVertices范围内才会添加
            如：
                numVertices = 6， 0-5范围内会添加顶点
            vtx: 范围，表示当前是第几个顶点
            id: 顶点的标识
        """
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setVertexID(id)
    
    def getVertex(self, n):
        """获取某一个顶点
            n: 顶点标识
            return: 该顶点是第几个顶点，没找到则返回None
        """
        for vertxin in range(self.numVertices):
            if n == self.vertices[vertxin].getVertexID():
                return vertxin
        return None

    def addEdge(self, frm, to, cost=0):
        """添加一条边
            frm: 开始顶点
            to: 终止顶点
            cost: 代价，默认为0
        """
        if self.getVertex(frm) is not None and self.getVertex(to) is not None:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
            if not self.directed:
                self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost

    def getVertices(self):
        """获取全部的顶点
            return: 顶点id组成的列表
        """
        vertices = []
        for vertxin in range(self.numVertices):
            vertices.append(self.vertices[vertxin].getVertexID())
        return vertices
    
    def printMatrix(self):
        """打印邻接矩阵
            "/" 表示两个顶点之间没有边
        """
        for u in range(self.numVertices):  # 行索引
            row = []
            for v in range(self.numVertices):  # 列索引
                row.append(str(self.adjMatrix[u][v]) if self.adjMatrix[u][v] is not None else "/")
            print(row)
    
    def getEdges(self):
        """获取所有的边
            return: 返回包含(起点，终点，花费)的列表，列表中的元素都是元组
        """
        edges = []
        for v in range(self.numVertices):
            for u in range(self.numVertices):
                if self.adjMatrix[u][v] is not None:  # 按列遍历
                    vid = self.vertices[v].getVertexID()
                    uid = self.vertices[u].getVertexID()
                    edges.append((uid, vid, self.adjMatrix[u][v]))
        return edges

    def getNeighbors(self, n):
        """获取顶点的邻居顶点
            仅计算起点为n的边
        """
        neighbors = []
        for vertxin in range(self.numVertices):
            if n == self.vertices[vertxin].getVertexID():
                for neighbor in range(self.numVertices):
                    if self.adjMatrix[vertxin][neighbor] is not None:
                        neighbors.append(self.vertices[neighbor].getVertexID())
        return neighbors

    def isConnected(self, u, v):
        """判断两个顶点是否连通
        """
        uid = self.getVertex(u)
        vid = self.getVertex(v)
        return self.adjMatrix[uid][vid] is not None
    
    def get2Hops(self, u):
        """找到距离顶点u两步的顶点
        """
        neighbors = self.getNeighbors(u)
        print(neighbors)
        hopset = set()
        for v in neighbors:
            hops = self.getNeighbors(v)
            hopset |= set(hops)  # 集合的按位或运算是取并集
        return list(hopset)


if __name__ == "__main__":
    graph = Graph(6, True)
    graph.addVertex(0, "a")
    graph.addVertex(1, "b")
    graph.addVertex(2, "c")
    graph.addVertex(3, "d")
    graph.addVertex(4, "e")
    graph.addVertex(5, "f")
    # print(graph.getVertex("e"))
    # print(graph.getVertices())
    graph.addEdge('a', 'b', 1)
    graph.addEdge('a', 'c', 2)
    graph.addEdge('b', 'd', 3)
    graph.addEdge('b', 'e', 4)
    graph.addEdge('c', 'd', 5)
    graph.addEdge('c', 'e', 6)
    graph.addEdge('d', 'e', 7)
    graph.addEdge('e', 'a', 8)
    # graph.printMatrix()
    # print(graph.getEdges())
    # print(graph.getNeighbors("a"))
    print(graph.get2Hops("b"))