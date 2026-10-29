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

def iddfs(graph, start, max_depth):
    for depth in range(max_depth + 1):
        print(f"Depth {depth}:", end=" ")
        dls(graph, start, depth)
        print()

iddfs(graph, 'A', 2)