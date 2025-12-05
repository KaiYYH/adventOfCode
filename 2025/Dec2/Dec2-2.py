import re, textwrap
input, Part2 = open("Dec2Input.txt", "r"), 0

for i in input: 
    ids = re.findall(r'(\d+)-(\d+)', i)

for pair in ids: 
    for id in range(int(pair[0]), int(pair[1]) + 1):
        for value in range(1, (len(str(id)) // 2) + 1):
            if len(str(id)) % value == 0: 
                groups = textwrap.wrap(str(id), value)
                if len(set(groups)) == 1:
                    Part2 += id
                    break

print("Part 2: " + str(Part2))