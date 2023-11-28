"""1. Depth-First Search (DFS)
DFS is a traversal algorithm that goes as deep as possible in one branch before backtracking. It can be implemented using recursion or a stack.

DFS Example Code (Recursive)
"""

def dfs_iterative(graph, start):
    visited = list()  # I use a list to keep order so we can test at the end the order
    stack = [start]

    while stack:
        print('stack: ', stack)
        node = stack.pop()

        if node not in visited:
            print('node visited: ', node)
            visited.append(node)
            for neighbor in graph[node]:
                print('adding neighbor: ', neighbor)
                stack.append(neighbor) # add everything but the gaurd visited will not do anything if we visited

    return visited

# Example graph
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

# Testing the DFS iterative function
print("visited order ======>: ", dfs_iterative(graph, 'A'))  # Starting from node 'A')

print('substraction list: ', set([1,2]) - set([1]))
print('substraction list with strings: ', set(['A','B']) - set(['B']))
