import re
input, pattern, grid, count = open("Dec6.txt", "r"), re.compile(r"(turn on|turn off|toggle)\s+(\d+),(\d+)\s+through\s+(\d+),(\d+)"), [[0 for _ in range(1000)] for _ in range(1000)], 0

def f(grid, string):
    action, x1, y1, x2, y2 = pattern.match(string).groups()
    for x in range(int(y1), int(y2) + 1):
        for y in range(int(x1), int(x2) + 1):
            grid[x][y] += 1 if action == "turn on" else 2 if action == "toggle" else -1 if grid[x][y] > 0 else 0
    return grid

for i in input: grid = f(grid, i)
for row in grid: count += sum(row)

print("Part 2: " + str(count))