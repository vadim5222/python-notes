def all_paths(graph, start, end, path=None, visited=None):
    if path is None: path = []
    if visited is None: visited = set()
    path = path + [start]
    visited.add(start)
    if start == end:
        return [path]
    paths = []
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_paths = all_paths(graph, neighbor, end, path, visited.copy())
            paths.extend(new_paths)
    return paths

graph = {1: [2, 3], 2: [4, 5], 3: []}
print(all_paths(graph, 1, 4))
