input, diagram, count = open("Dec7.txt", "r"), [], 0

for i in input: 
    diagram.append(i.replace("\n", ""))

string = diagram[0].replace("S", "|")

for row in diagram: 
    for character in range(len(row)): 
        if row[character] == "^" and string[character] == "|": 
            string = string[:character - 1] + "|.|" + string[character + 2:]
            count += 1

print("Part 1: " + str(count))