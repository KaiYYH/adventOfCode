input = open("Dec1Input.txt", "r")
floor = 0
position = 0

for i in input: 
    for x in i: 
        position += 1
        if x == "(": 
            floor += 1
        elif x == ")": 
            floor -= 1

        if floor == -1: 
            basementFloor = position
            break

print("Part 2: " + str(basementFloor))