import re
input = open("Dec2Input.txt", "r")
Part1 = 0

for i in input: 
    ids = re.findall(r'(\d+)-(\d+)', i)

for pair in ids: 
    for id in range(int(pair[0]), int(pair[1]) + 1):
        if len(str(id)) % 2 == 0: 
            groups = [str(id)[:int(len(str(id))/2)], str(id)[int(len(str(id))/2):]]
            if len(set(groups)) == 1: Part1 += id

print("Part 1: " + str(Part1))

