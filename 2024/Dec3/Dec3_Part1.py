import re
input = open('Dec3_Input.txt', 'r')

sum = 0

for line in input: 
    string = line

    pairs = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", string)

    for i in pairs: 
        sum += int(i[0]) * int(i[1])

print("Part 1: " + str(sum))