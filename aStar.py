from queue import PriorityQueue

graph = {
    'S':{'A':3,'D':4},
  'A' : {'B':4,'D':5},
  'B' : {'C':4,'E':5},
  'C' : {'B':4},
  'D' : {'A':5,'E':2},
  'E' : {'B':5,'F':4},
  'F' : {'G':3},
  'G':{'F':3}
}

heuristic={'S':11.0,'A':10.4,'B':6.7,'C':4.0,'D':8.9,'E':6.9,'F':3.0,'G':0}
visited = []
cost=0
queue=PriorityQueue()

def ufs(visited, graph, node,goal):
  global heuristic
  visited.append(node)
  queue.put((heuristic[node],node))
  print("Start : ",node)
  while queue:
    c,n = queue.get()
    if n not in visited:
        print(n)
        visited.append(n)
    if n==goal:
            return c
    for i in graph[n]:
      if graph[n][i] not in visited:
        tCost=(c-heuristic[n])+graph[n][i]+heuristic[i]
        queue.put((tCost,i))

b=ufs(visited,graph,'S','G')
print("Cost for above function : ",b)

