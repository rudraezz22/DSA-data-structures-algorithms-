def dijkstras(graph,start):
    node = list(graph.keys())
    distance = {}

    for i in node:
        distance[i]=999999

    distance[start]=0
    visited=[]

    while len(visited)<len(node):
        minnode=None
        mindistance=999999
        

        for j in node:
            if j not in visited and distance[j]<mindistance:
                mindistance = distance[j]
                minnode=j

        if minnode is None:
            break

        for n,weight in graph[minnode]:
            if n not in visited:
                ndistance = distance[minnode]+weight
                if ndistance<distance[n]:
                    distance[n] = ndistance
        visited.append(minnode)
    return distance

graph = {
    "A":[("B",1),("C",4)],
    "B":[("A",1),("C",2),("D",5)],
    "C":[("A",4),("B",2),("D",1)],
    "D":[("B",5),("C",1)]

}
start = "A"
u = dijkstras(graph,start)

for i in u:
    print(f"the distance of {start} to {i} is {u[i]}")