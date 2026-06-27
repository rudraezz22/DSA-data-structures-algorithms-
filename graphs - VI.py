#no. of trees in a forest

def add_edge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def dfs(u,adj,visited):
    visited[u] = True
    for i in range(len(adj[u])):
        if visited[adj[u][i]] == False:
            dfs(adj[u][i],adj,visited)


def count(adj,V):
    visited = [False]*V
    res = 0
    for u in range(V):
        if visited[u]==False:
            dfs(u,adj,visited)
            res+=1

    return res


V = 6
adjnum=[[] for i in range(V)]
add_edge(adjnum,0,1)
add_edge(adjnum,0,2)

add_edge(adjnum,0,3)

add_edge(adjnum,4,5)

print(count(adjnum,V))

#no. of rabbits with same color

def rabbits(answers,N):
    map = {}

    for a in range(N):
        if answers[a] in map:
            map[answers[a]]+=1
        else:
          map[answers[a]]=1


    count = 0
    for a in map:
        x = a
        y = map[a]

        if (y%(x+1))==0:
            count = count+((y//(x+1))*(x+1))
        else:
            count = count+((y//(x+1)+1)*(x+1))

    return count

arr = [2,2,0,0]
N=len(arr)
print(rabbits(arr,N))


