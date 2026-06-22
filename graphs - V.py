class graph:
    def __init__(self,V):
        self.V=V
        self.adjlist = [[] for i in range(V)]

    def add_edge(self,u,v):
        self.adjlist[u].append(v)

    def dfs(self,s):
        visited = [False for i in range(self.V)]
        stack = []
        stack.append(s)
        while len(stack):
            s = stack[-1]
            
            stack.pop()

            if not visited[s]:
                print(s,end=" ")
                visited[s] = True

            for node in self.adjlist[s]:
                if not visited[node]:
                    stack.append(node)


g = graph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,4)
g.dfs(0)


