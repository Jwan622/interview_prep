"""
the "Number of Islands" problem is a classic LeetCode question often used in technical interviews, including potentially at companies like DoorDash. It's a great problem to showcase your understanding of Depth-First Search (DFS) algorithms. Here's an outline of the problem:

Problem Statement: Number of Islands
Given a 2D grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

input:
11110
11010
11000
00000

output: 1 island

exmaple:
11000
11000
00100
00011

output: 3 islands

Approach using DFS
The main idea is to iterate through each cell of the grid. When we encounter a '1', we start a DFS from that cell, marking all adjacent '1's as visited, effectively "sinking" that piece of the island. We then continue scanning through the grid for the next unvisited '1' to start a new DFS, which would represent a new island.

Here's a high-level algorithm:

Iterate over each cell in the grid.
If a cell with '1' is found, increment the island count.
Start DFS from that cell, and mark all reachable '1's as visited (can be done by setting them to '0' or using a separate visited matrix).
Continue the scan to find the next '1'.

DFS Function
The DFS function will:

Check the current cell's boundaries and whether it's already visited.
Recursively call DFS for all adjacent cells (up, down, left, right) that are part of the island ('1').
"""

grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "1"]
]


def num_islands(grid):
    if not grid:
        return 0

    def dfs(y_coord, x_coord): # this is depth first because even though there is no stack variable, we keep going depth/down an island block until we return.
        print('this loop x and y: ', x_coord, y_coord)
        if y_coord < 0 or x_coord < 0 or y_coord >= len(grid) or x_coord >= len(grid[0]) or grid[y_coord][x_coord] == '0': # off the map or off the island
            print('in the return block', x_coord, y_coord)
            return
        print('setting to 0: ', x_coord, y_coord)
        grid[y_coord][x_coord] = '0'
        print("calling dfs(y_coord + 1, x_coord)")
        dfs(y_coord + 1, x_coord)
        print("calling dfs(y_coord - 1, x_coord)")
        dfs(y_coord - 1, x_coord)
        print("calling dfs(y_coord, x_coord + 1)")
        dfs(y_coord, x_coord + 1)
        print("calling dfs(y_coord, x_coord - 1)")
        dfs(y_coord, x_coord - 1)

    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '1':  # if a 1, run dfs. Basically what this does is check all the up, down, left, and right around a 1 until it's exhausted and flipped to 0, and then we increment the count.
                dfs(y, x)
                print('COUNT INCREMENTING ==================>: ', x, y)
                count += 1

    return count


print("grid1: ", num_islands(grid1))
print("grid2: ", num_islands(grid2))
