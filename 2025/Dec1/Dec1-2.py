input = open("Dec1Input.txt", "r")
dial = 50
Part2 = 0

for i in input:
    for click in range(int(i[1:])):
        dial = (dial + 1) % 100 if i[0] == "R" else (dial - 1) % 100
            
        if dial == 0:
            Part2 += 1

print("Part 2: " + str(Part2))