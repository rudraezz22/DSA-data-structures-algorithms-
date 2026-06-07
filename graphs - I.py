

#GRAPH BY ARRAY
class GRAPH:
    def __init__(self):
        self.graph = {}
    
    def addedge(self,u,v):
        self.graph.setdefault(u,[]).append(v)
        self.graph.setdefault(v,[]).append(u)

    def display(self):
        for i in self.graph:
            print(i,self.graph[i])

g2 = GRAPH()

g2.addedge(0,1)
g2.addedge(1,2)
g2.addedge(2,3)
g2.addedge(3,4)
g2.display()