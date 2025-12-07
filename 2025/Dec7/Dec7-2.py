input, diagram, current, timelines = open("Dec7.txt", "r"), [], [], 0

for i in input: 
    diagram.append(i.replace("\n", ""))

for character in diagram[0]: 
    current.append(1) if character == "S" else current.append(0)

for row in diagram: 
    for character in range(len(row)): 
        if row[character] == "^" and current[character] > 0:
            current[character - 1] += current[character]
            current[character + 1] += current[character]
            current[character] = 0

print("Part 2: " + str(sum(current)))