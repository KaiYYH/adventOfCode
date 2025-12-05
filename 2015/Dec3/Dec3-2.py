input, loc, santa_x, santa_y, robo_x, robo_y = open("Dec3.txt", "r"), [(0, 0)], 0, 0, 0, 0
dirs = {"^": [0, 1], ">": [1, 0], "v": [0, -1], "<": [-1, 0]}

for i in input: 
    for dir in range(len(i)): 
        if dir % 2 == 0: 
            santa_x += dirs[i[dir]][0]
            santa_y += dirs[i[dir]][1]
            loc.append((santa_x, santa_y))
        else: 
            robo_x += dirs[i[dir]][0]
            robo_y += dirs[i[dir]][1]
            loc.append((robo_x, robo_y))

print("Part 2: " + str(len(set(loc))))