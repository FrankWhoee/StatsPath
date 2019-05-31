
def neighbours(grid, node):
    output = []
    output.append((node[0], node[1] + 1))
    output.append((node[0], node[1] - 1))
    output.append((node[0] + 1, node[1]))
    output.append((node[0] - 1, node[1]))
    for index in range(output.__len__()-1,-1,-1):
        pos = output[index]
        if pos[0] < 0 or pos[0] >= grid.__len__() or pos[1] < 0 or pos[1] >= grid[0].__len__() or grid[pos[0]][pos[1]] == 1:
            output.remove(pos)
    return output

def heuristic(a, b):
    # Manhattan distance on a square grid
    return abs(a[0] - b[0]) + abs(a[1] - b[1])