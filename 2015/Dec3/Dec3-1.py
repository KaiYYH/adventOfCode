input, loc, x, y = open("Dec3.txt", "r"), [(0, 0)], 0, 0
dirs = {"^": [0, 1], ">": [1, 0], "v": [0, -1], "<": [-1, 0]}

for i in input: 
    for dir in i: 
        x += dirs[dir][0]
        y += dirs[dir][1]
        loc.append((x, y))

print("Part 1: " + str(len(set(loc))))