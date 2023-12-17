class Vertex:
    def __init__(self, key):
        self.key = key

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class Graph:
    def __init__(self, adj_map):
        self.adj_map = adj_map

def DFS(graph, vertex, visited=None):
    if visited is None:
        visited = {}

    # Mark the current vertex as visited
    visited[vertex] = None

    # Recur for all the adjacent vertices
    for neighbor in graph.adj_map[vertex]:
        if neighbor not in visited:
            visited[neighbor] = vertex
            DFS(graph, neighbor, visited)

    return visited
