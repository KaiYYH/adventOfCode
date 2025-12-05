input = open("Dec1Input.txt", "r")
dial, Part1 = 50, 0

for i in input:
    dial = (dial + int(i[1:])) % 100 if i[0] == "R" else (dial - int(i[1:])) % 100
    if dial == 0: Part1 += 1

print("Part 1: " + str(Part1))