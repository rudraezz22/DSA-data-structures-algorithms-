V=4
INF=99999

def floydwarshall(graph):
    dist=[row[:] for row in graph]
    for k in range(V): #for intermidiate
        for i in range(V):#for source
            for j in range(V):#for target
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    printfloyd(dist)

def printfloyd(dist):
    for i in range(V):
        for j in range(V):
            if dist[i][j]==INF:
                print("inf",end=" ")
            else:
                print("%7d"%dist[i][j],end=" ")
        print(" ")

     
graph=[
    [0,5,INF,10],
    [INF,0,3,INF],
    [INF,INF,0,1],
    [INF,INF,INF,0]
       ]

floydwarshall(graph)