def dfs(graph,start,visited = None):
    if visited is None:
      visited = set()

    print(start,end=" ")
    visited.add(start)

    for neighbour in graph[start]:
       if neighbour not in visited:
          
          dfs(graph,neighbour,visited)

g = {
   "A":["B","C"],
   "B":["A","D","E"],
   "C":["A","F"],
   "D":["B"],
   "E":["B","F"],
   "F":["C","E"],

}
dfs(g,"A")

#using stack - lifo


#using stack - lifo


#using stack - lifo
def dfs1(graph,start):
   visited = []
   stack = [start]

   while stack:
      node = stack.pop()

      if node not in visited:
         visited.append(node)
         for neighbours in reversed(graph[node]):
            stack.append(neighbours)

   return visited

g1 = {
   "A":["B","C"],
   "B":["A","D","E"],
   "C":["A","F"],
   "D":["B"],
   "E":["B","F"],
   "F":["C","E"],

}
print(dfs1(g1,"A"))