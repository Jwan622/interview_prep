"""2. Breadth-First Search (BFS)
BFS is a traversal algorithm that explores all neighbors at the present depth before moving on to the nodes at the next depth level. It typically uses a queue.
"""

from collections import deque


def bfs(graph, start):
    visited, queue = set(), deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)



graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


# Example usage
bfs(graph, 'A')  # Starting from node 'A'
