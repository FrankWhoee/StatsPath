import numpy as np
import collections
from util.path_utils import neighbours

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
graph = np.array([[0, 0, 0, 1],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0],
                  [1, 0, 0, 0]])


# Clear = 0
# Filled = 1

def bfs_pathing(graph, start, goal, return_animation=False):

    if return_animation:
        animation = [graph.copy()]
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break
        for next in neighbours(graph, current):
            if next not in came_from:
                if return_animation:
                    graph_copy = animation[animation.__len__() - 1].copy()
                    graph_copy[next[0]][next[1]] = 2
                    animation.append(graph_copy)
                frontier.put(next)

                came_from[next] = current
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    if return_animation:
        for pos in path:
            graph_copy = animation[animation.__len__() - 1].copy()
            graph_copy[pos[0]][pos[1]] = 3
            animation.append(graph_copy)
        return path, animation
    return path
