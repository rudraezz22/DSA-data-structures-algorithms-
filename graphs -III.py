
from collections import defaultdict

class graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def bfs(self,start):
        visited = [False]*(max(self.graph)+1)
        queue = []
        queue.append(start)
        visited[start] = True
     
        while queue:
            node = queue.pop(0)
            print(node,end=" ")

            for neighbour in self.graph[node]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True


g = graph()
g.add_edge(11,12)
g.add_edge(11,13)
g.add_edge(12,13)
g.add_edge(13,11)
g.add_edge(12,11)
g.add_edge(13,13)
g.bfs(12)


#using deque library
from collections import deque
def bfs(graph,start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex  = queue.popleft()
        print(vertex,end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)


d1 = {
    "A" : ["B","C"],
    "B" : ["A","D","E"],
    "C" : ["A","F"],
    "D" : ["B"],
    "E" : ["B","F"],
    "F" : ["E","C"]
}

bfs(d1,"A")