class Graph:
  def __init__(self,v):
    self.graph = []
    self.v=v

  def add_edge(self,u,v,w):
    self.graph.append([u,v,w])

  def printdist(self,dist):
    for i in range(self.v):
      print("{0}\t\t{1}".format(i,dist[i]))

  def bellmanFord(self,src):
    dist = [float("Inf")]*self.v
    dist[src]=0

    for _ in range(self.v-1):
      for u,v,w in self.graph:
        if dist[u] !=float("Inf") and dist[u]+w<dist[v]:
          dist[v]=dist[u]+w


    for u,v,w in self.graph:
      if dist[u] !=float("Inf") and dist[u]+w<dist[v]:
        print("no negative cycles found")
        return
      
    self.printdist(dist)


g = Graph(5)
g.add_edge(0,1,-1)
g.add_edge(0,2,4)
g.add_edge(1,2,3)
g.add_edge(1,3,2)
g.add_edge(1,4,2)
g.add_edge(3,2,5)
g.add_edge(3,1,1)
g.add_edge(4,3,-3)

g.bellmanFord(0)
