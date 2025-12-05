input, grid, adjacent, rolls, Part2 = open("Dec4Input.txt", "r"), [], [[0, 1], [0, -1], [1, 1], [1, 0], [1, -1], [-1, 1], [-1, 0], [-1, -1]], True, 0

def adjacent_roll(grid, x, y): 
    return x in range(len(grid)) and y in range(len(grid[x])) and grid[x][y] == "@"

def accessible(grid, adjacent, x, y): 
    count = 0
    for adj in adjacent: 
        if adjacent_roll(grid, x + adj[0], y + adj[1]): count += 1
    return count < 4

for i in input: 
    grid.append(i.replace("\n", ""))

while rolls == True: 
    rolls = False
    for x in range(len(grid)): 
        for y in range(len(grid[x])): 
            if grid[x][y] == "@" and accessible(grid, adjacent, x, y): 
                Part2 += 1
                grid[x], rolls = grid[x][:y] + "." + grid[x][y + 1:], True

print("Part 2: " + str(Part2))