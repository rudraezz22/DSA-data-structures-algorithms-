def sink_nodes(g):
  
    sinks = []
    for i in g:
      if g[i]==[]:
        sinks.append(i)

    return sinks

g = {
   "A":["B","C"],
   "B":["A","D","E"],
   "C":["A","F"],
   "D":[],
   "E":["B","F"],
   "F":["C","E"],

}
sink_nodes(g)
