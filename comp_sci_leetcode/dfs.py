"""1. Depth-First Search (DFS)
DFS is a traversal algorithm that goes as deep as possible in one branch before backtracking. It can be implemented using recursion or a stack.

DFS Example Code (Recursive)
"""

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        print('stack: ', stack)
        vertex = stack.pop()  # this always targets the last added vertex
        print('popped vertex: ', vertex)
        if vertex not in visited:  # do not do anything if we visited already
            print("we visited this vertex =============> ", vertex)
            visited.add(vertex)
            # Add neighbors to the stack
            stack.extend(graph[vertex] - visited)

# Example graph
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

# Testing the DFS iterative function
dfs_iterative(graph, 'A')  # Starting from node 'A'

print('substraction list: ', set([1,2]) - set([1]))
print('substraction list with strings: ', set(['A','B']) - set(['B']))
