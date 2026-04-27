from collections import deque

def bfs(a, b, target):
    visited = set()
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print((x, y))   # ✅ print only once

        # check target
        if x == target or y == target:
            return "Target Reached"

        # possible moves
        q.append((a, y))   # fill A
        q.append((x, b))   # fill B
        q.append((0, y))   # empty A
        q.append((x, 0))   # empty B

        # pour A → B
        pour = min(x, b - y)
        q.append((x - pour, y + pour))

        # pour B → A
        pour = min(y, a - x)
        q.append((x + pour, y - pour))

    return "Not Possible"


# Run
print(bfs(4, 3, 2))