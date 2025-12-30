import shapely
input, red, green, pairs, largest = open("Dec9.txt", "r"), [], [], [], 0

for i in input: 
    red.append([int(n) for n in i.strip().split(",")])
green = shapely.Polygon(red)

for point1 in range(len(red)): 
    for point2 in range(point1 + 1, len(red)): 
        x1, y1 = red[point1]
        x2, y2 = red[point2]
        minx, maxx, miny, maxy = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
        redShape = shapely.Polygon([(minx, miny), (minx, maxy), (maxx, maxy), (maxx, miny)])
        area = (abs(red[point2][1] - red[point1][1]) + 1) * (abs(red[point2][0] - red[point1][0]) + 1)
        if area > largest and green.covers(redShape): 
            largest = area

print("Part 2: " + str(largest))