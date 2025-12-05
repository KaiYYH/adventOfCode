input, grid, adjacent, Part1 = open("Dec4Input.txt", "r"), [], [[0, 1], [0, -1], [1, 1], [1, 0], [1, -1], [-1, 1], [-1, 0], [-1, -1]], 0

def adjacent_roll(grid, x, y): 
    return x in range(len(grid)) and y in range(len(grid[x])) and grid[x][y] == "@"

def accessible(grid, adjacent, x, y): 
    count = 0
    for adj in adjacent: 
        if adjacent_roll(grid, x + adj[0], y + adj[1]): count += 1
    return count < 4

for i in input: 
    grid.append(i.replace("\n", ""))

for x in range(len(grid)): 
    for y in range(len(grid[x])): 
        if grid[x][y] == "@" and accessible(grid, adjacent, x, y): Part1 += 1

print("Part 1: " + str(Part1))