def astar(graph, h, start, goal):
    open_list = [start]
    closed = []

    g = {start: 0}          # cost from start
    parent = {start: None}  # to reconstruct path

    while open_list:
                                                                    # node with lowest f = g + h
        n = min(open_list, key=lambda x: g[x] + h[x])

                                                                    # goal reached → reconstruct path
        if n == goal:
            path = []
            while n is not None:
                path.append(n)
                n = parent[n]
            return path[::-1], g[goal]

        open_list.remove(n)
        closed.append(n)

                                                                     # explore neighbors
        for (m, cost) in graph[n]:
            if m not in open_list and m not in closed:
                open_list.append(m)
                parent[m] = n
                g[m] = g[n] + cost

            else:
                if g[m] > g[n] + cost:
                    g[m] = g[n] + cost
                    parent[m] = n

                    if m in closed:
                        closed.remove(m)
                        open_list.append(m)

    return None, None


# Graph definition
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

# Heuristic values
h = {'A': 4, 'B': 2, 'C': 1, 'D': 0}

# Run A*
path, cost = astar(graph, h, 'A', 'D')

print("Path:", path)
print("Cost:", cost)