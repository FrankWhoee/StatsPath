import numpy as np
from time import time
import heapq
from util.path_utils import neighbours,heuristic


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


# graph = np.zeros((50, 40))
graph = np.array([[0, 0, 0, 1],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0],
                  [1, 0, 0, 0]])


# Clear = 0
# Filled = 1


start = (0, 0)
goal = (3, 3)

frontier = PriorityQueue()
frontier.put(start, 0)
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
    current = frontier.get()

    if current == goal:
        break

    for next in neighbours(graph,current):
        new_cost = cost_so_far[current]
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost + heuristic(goal, next)
            frontier.put(next, priority)
            came_from[next] = current
current = goal
path = []
while current != start:
    path.append(current)
    current = came_from[current]
path.append(start)  # optional
path.reverse()  # optional

print(path)
