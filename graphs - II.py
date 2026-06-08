
class graph:
    def __init__(self,num_vertices):
        self.num_vertices = num_vertices
        self.adjlist  = [[i] for i in range(self.num_vertices)]

    def add_edge(self,u,v):
        self.adjlist[u].append(v)

    def display(self):
        for i in range(self.num_vertices):
            print(i,"->",self.adjlist[i])
g = graph(5)

g.add_edge(0,1)
g.add_edge(1,0)
g.add_edge(2,1)
g.add_edge(3,2)
g.add_edge(4,3)

g.display()
#representation of graph using adjlist

class ADJlist:
    def __init__(self,data):
        self.vertex = data
        self.next = None

class graph1:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices

    def add_edge(self,src,dest):
        node = ADJlist(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

        node = ADJlist(dest)
        node.next = self.graph[src]
        self.graph[src] = node


    def print1(self):
        for i in range(self.vertices):
            print("adjlist at particular vertex i {}".format(i),end = " ")
            temp = self.graph[i]

            while temp:
                print("-> {}".format(temp.vertex),end = " ")
                temp = temp.next

            print("\n")

g2 = graph1(5)
g2.add_edge(0,1)
g2.add_edge(1,0)
g2.add_edge(2,1)
g2.add_edge(3,2)
g2.add_edge(4,3)
g2.print1()
