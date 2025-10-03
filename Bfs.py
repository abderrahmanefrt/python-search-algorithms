from collections import deque



def  Bfs(s,succesor,goal):
  queue=deque([s])
  closed=[]

  while queue:
    current=queue.popleft() 
    print(f"Visite: {current}")
    if goal== current:
      print(f"Goal found: {current}") 
      return current
    
    for s in succesor(current):
      if s not in closed:
        closed.append(s)
        queue.append(s)


  print("Not found") 
  return False     


graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['J'],
    'J': ['K'],
    'K': []
}

def succesor(node):
    return graph.get(node, [])


Bfs('A', succesor, 'K') 



