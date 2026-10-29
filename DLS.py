graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dls(graph, node, limit, depth=0):
    print(node, end=" ")

    if depth == limit:
        return

    for neighbor in graph[node]:
        dls(graph, neighbor, limit, depth + 1)

print("DLS Traversal:")
dls(graph, 'A', 2)
print()