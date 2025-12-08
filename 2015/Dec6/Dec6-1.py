import re
input, pattern, grid, count = open("Dec6.txt", "r"), re.compile(r"(turn on|turn off|toggle)\s+(\d+),(\d+)\s+through\s+(\d+),(\d+)"), [["x" for _ in range(1000)] for _ in range(1000)], 0

def f(grid, string):
    action, x1, y1, x2, y2 = pattern.match(string).groups()
    for x in range(int(y1), int(y2) + 1):
        for y in range(int(x1), int(x2) + 1):
            grid[x][y] = "o" if action == "turn on" else "x" if action == "turn off" else "o" if grid[x][y] == "x" else "x"
    return grid

for i in input: grid = f(grid, i)
for row in grid: count += row.count("o")

print("Part 1: " + str(count))