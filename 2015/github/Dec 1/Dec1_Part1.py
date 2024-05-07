input = open("Dec1Input.txt", "r")
floor = 0

for i in input: 
    for x in i: 
        if x == "(": 
            floor += 1
        elif x == ")": 
            floor -= 1

print("Part 1: " + str(floor))