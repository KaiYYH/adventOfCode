input = open("Dec3Input.txt", "r")
Part2 = 0

for i in input: 
    joltage = i.replace('\n', '')
    x = 0
    y = 1
    while len(joltage) > 12: 
        if joltage[x] < joltage[y]: 
            joltage = joltage[:x] + joltage[y:]
            x = 0
            y = 1
        elif y == len(joltage) - 1: 
            joltage = joltage[:-1]
            x = 0
            y = 1
        else: 
            x += 1
            y += 1
    
    Part2 += int(joltage)

print("Part2: " + str(Part2))