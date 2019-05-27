import queue

def neighbours(grid,node):
   output = []
   output.append(grid[node[0]][node[1] + 1])
   output.append(grid[node[0]][node[1] - 1])
   output.append(grid[node[0] + 1][node[1]])
   output.append(grid[node[0] - 1][node[1]])

start = (0,0)
goal = (0,0)

frontier = queue()
frontier.put(start )
came_from = {}
came_from[start] = None

while not frontier.empty():
   current = frontier.get()

   if current == goal:
      break

   for next in graph.neighbors(current):
      if next not in came_from:
         frontier.put(next)
         came_from[next] = current