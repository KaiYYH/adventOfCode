import re
input = open("Dec5Input.txt", "r")
ranges, ingredients, Part1 = [], [], 0

for i in input: 
    if "-" in i: 
        ranges.append([int(n) for n in re.findall(r'\d+', i)])
    elif i != "\n": 
        ingredients.append(int(i.replace("\n", "")))

for ingredient in ingredients: 
    for range in ranges: 
        if ingredient >= range[0] and ingredient <= range[1]: 
            Part1 += 1
            break

print("Part 1: " + str(Part1))