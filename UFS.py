from queue import PriorityQueue

graph = {
  'A' : {'B':21,'C':25},
  'B' : {'D':38,'E':29},
  'C' : {'F':3},
  'D' : {'E':9},
  'E' : {'F':2},
  'F' : {}
}

visited = []
cost=0
queue=PriorityQueue()

def ufs(visited, graph, node,goal):
  visited.append(node)
  queue.put((0,node))
  while queue:
    c,n = queue.get()
    print(n," Cost : ",c)
    if n not in visited:
        print(n)
        visited.append(n)
    if n==goal:
            return c
    for i in graph[n]:
      if graph[n][i] not in visited:
        tCost=c+graph[n][i]
        queue.put((tCost,i))
b=ufs(visited,graph,'A','F')
print("Cost for above function : ",b)

