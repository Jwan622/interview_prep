"""2. Breadth-First Search (BFS)
BFS is a traversal algorithm that explores all neighbors at the present depth before moving on to the nodes at the next depth level. It typically uses a queue.
"""

from collections import deque


def bfs(graph, start):
    visited = list()
    queue = deque([start])

    while queue:
        print('queue: ', queue)
        node = queue.popleft()
        print('node: ', node)

        if node not in visited:
            print('visiting =============> ', node)
            visited.append(node)
            for neighbor in graph[node]:
                queue.append(neighbor)

    return visited


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}


# Example usage
bfs(graph, 'A')  # Starting from node 'A'
