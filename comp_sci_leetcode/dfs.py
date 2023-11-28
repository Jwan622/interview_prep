"""1. Depth-First Search (DFS)
DFS is a traversal algorithm that goes as deep as possible in one branch before backtracking. It can be implemented using recursion or a stack.

DFS Example Code (Recursive)
"""

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

# xample usage
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

dfs(graph, 'A')  # Starting from node 'A'
