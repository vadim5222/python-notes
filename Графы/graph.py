# =======================================BFS
# from collections import deque

# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#     visited.add(start)
#     result = []

#     while queue:
#         node = queue.popleft()
#         result.append(node)

#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)
#     return result


# graph = {
#     'A':['B', 'C'],
#     'B':['A', 'D'],
#     'C':['A', 'D'],
#     'D':['B', 'C'],
# }

# print(bfs(graph, 'A'))



# ============================================DFS
# def dfs(graph, node, visited=None):
#     if visited is None:
#         visited = set()

#     visited.add(node)
#     result = [node]

#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             result.extend(dfs(graph, neighbor, visited))

#     return result


# graph = {
#     'A':['B', 'C'],
#     'B':['A', 'D'],
#     'C':['A', 'D'],
#     'D':['B', 'C'],
# }
# print(dfs(graph, 'A'))

# =========================================================Топологическая сортировка
# from collections import deque

# def topological_sort(graph, in_degree):
#     queue = deque([node for node in graph if in_degree[node] == 0])
#     result = []


#     while queue:
#         node = queue.popleft()
#         result.append(node)

#         for neighbor in graph[node]:
#             in_degree[neighbor] -= 1
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)
#     return result

# graph = {
#     'A':['B', 'C'],
#     'B':['D'],
#     'C':['D'],
#     'D':[]
# }

# in_degree = {'A':0, 'B':1, 'C':1, 'D':3}
# print(topological_sort(graph, in_degree))