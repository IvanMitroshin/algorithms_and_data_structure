from collections import deque

class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append(v)

graph = DirectedGraph()
graph.add_vertex(1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 1)
print(graph.graph)


def bfs(graph, start):
    n = set()
    queue = deque([start])
    n.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for i in graph.graph[vertex]:
            if i not in n:
                n.add(i)
                queue.append(i)

def matrix_edge(edges):
    vertices = set()
    for u, v in edges:
        vertices.add(u)
        vertices.add(v)
    n = len(vertices)
    matrix = [[0] * n for _ in range(n)]
    vertex_index = {vertex: i for i, vertex in enumerate(vertices)}
    for u, v in edges:
        matrix[vertex_index[u]][vertex_index[v]] = 1
    return matrix, vertex_index