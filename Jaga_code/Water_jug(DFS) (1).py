def dfs(x, y, a, b, target, visited):
    if (x, y) in visited:
        return False

    visited.add((x, y))   # ✅ mark first
    print((x, y))         # print state

    # check target
    if x == target or y == target:
        return True

    # recursive DFS calls
    return (
        dfs(a, y, a, b, target, visited) or        # fill A
        dfs(x, b, a, b, target, visited) or        # fill B
        dfs(0, y, a, b, target, visited) or        # empty A
        dfs(x, 0, a, b, target, visited) or        # empty B
        dfs(max(0, x-(b-y)), min(b, x+y), a, b, target, visited) or  # A → B
        dfs(min(a, x+y), max(0, y-(a-x)), a, b, target, visited)     # B → A
    )


# Run
if dfs(0, 0, 4, 3, 2, set()):
    print("Target Reached")
else:
    print("Not Possible")