import numpy as np
import collections


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


# graph = np.zeros((50, 40))
graph = np.array([[0, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0],
                  [1, 0, 0, 0]])


# Clear = 0
# Filled = 1

def neighbours(grid, node):
    output = []
    output.append((node[0], node[1] + 1))
    output.append((node[0], node[1] - 1))
    output.append((node[0] + 1, node[1]))
    output.append((node[0] - 1, node[1]))

    for index, pos in enumerate(output.__reversed__()):
        if pos[0] < 0 or pos[0] >= grid.__len__() or pos[1] < 0 or pos[1] >= grid[0].__len__() or grid[pos[0]][pos[1]] == 1:
            output.remove(pos)
            print(pos)
    return output


start = (0, 0)
goal = (3, 3)

frontier = Queue()
frontier.put(start)
came_from = {}
came_from[start] = None

while not frontier.empty():
    current = frontier.get()

    if current == goal:
        break
    # print(graph)
    # print(current)
    for next in neighbours(graph, current):
        if next not in came_from:
            frontier.put(next)
            came_from[next] = current
current = goal
path = []
while current != start:
    path.append(current)
    current = came_from[current]
path.append(start)  # optional
path.reverse()  # optional

print(path)
