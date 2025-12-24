input, red, pairs, largest = open("Dec9.txt", "r"), [], [], 0

for i in input: 
    red.append([int(n) for n in i.strip().split(",")])
for point1 in range(len(red)): 
    for point2 in range(point1 + 1, len(red)): 
        area = (abs(red[point2][1] - red[point1][1]) + 1) * (abs(red[point2][0] - red[point1][0]) + 1)
        if area > largest: 
            largest = area

print("Part 1: " + str(largest))