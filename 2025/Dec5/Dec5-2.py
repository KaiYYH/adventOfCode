import re
input = open("Dec5Input.txt", "r")
ranges, fresh, Part2 = [], [], 0

for i in input: 
    if "-" in i: ranges.append([int(n) for n in re.findall(r'\d+', i)])

sorted_ranges = sorted(ranges, key = lambda x: x[0])
x, y = 0, 1
while y < len(sorted_ranges): 
    if sorted_ranges[x][1] >= sorted_ranges[y][0] or sorted_ranges[x][1] >= sorted_ranges[y][1]: 
        sorted_ranges[x] = [sorted_ranges[x][0], max(sorted_ranges[x][1], sorted_ranges[y][1])]
        sorted_ranges.pop(y)
        x, y = 0, 1
    else: 
        x += 1
        y += 1
        
for range in sorted_ranges: 
    Part2 += range[1] - range[0] + 1

print("Part 2: " + str(Part2))