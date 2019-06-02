import heapq
from util.path_utils import neighbours, heuristic


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


# Clear = 0
# Filled = 1
# Visited = 2
# Start = 3
# Goal = 4
# Path = 5

def astar_pathing(graph, start, goal, return_animation=False):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    if return_animation:
        animation = [graph.copy()]
        animation[0][start[0]][start[1]] = 3
        animation[0][goal[0]][goal[1]] = 4

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in neighbours(graph, current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                if return_animation:
                    graph_copy = animation[animation.__len__() - 1].copy()
                    graph_copy[next[0]][next[1]] = 2
                    animation.append(graph_copy)
                frontier.put(next, priority)
                came_from[next] = current
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    if return_animation:
        for pos in path:
            graph_copy = animation[animation.__len__() - 1].copy()
            graph_copy[pos[0]][pos[1]] = 5
            animation.append(graph_copy)
        return path, animation
    return path
