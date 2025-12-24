import math
input, points, pairs = open("Dec8.txt", "r"), [], []

def findIndex(n): 
    for i, circuit in enumerate(circuits): 
        if n in circuit: 
            return i
    return None

for i in input: 
    points.append([int(n) for n in i.strip().split(",")])
for point1 in range(len(points)): 
    for point2 in range(point1 + 1, len(points)):
        pairs.append([math.dist(points[point1], points[point2]), [point1, point2]])
pairs.sort(reverse = True)
circuits = [{n} for n in range(len(points))]

while len(circuits) > 1: 
    p1, p2 = pairs.pop()[1]
    index1, index2 = findIndex(p1), findIndex(p2)
    if index1 != index2: 
        circuits[index1] = circuits[index1] | circuits [index2]
        del circuits[index2]

circuits.sort(key = lambda x: len(x))
print("Part 2: " + str(points[p1][0] * points[p2][0]))