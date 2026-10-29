import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}

def ucs(graph, start, goal):
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)
        print(f"Visited: {node}, Cost: {cost}")

        if node == goal:
            return cost

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (cost + edge_cost, neighbor)
                )

    return None

result = ucs(graph, 'A', 'G')
print("Minimum cost from A to G:", result)