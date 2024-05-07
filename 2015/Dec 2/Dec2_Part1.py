input = open("Dec2Input.txt", "r")
areas = []
wrapping = []

for i in input: 
    dimensions = i.split("x")
    areas = [int(dimensions[0])*int(dimensions[1]), int(dimensions[1])*int(dimensions[2]), int(dimensions[0])*int(dimensions[2])]
    wrapping.append(min(areas) + 2*areas[0] + 2*areas[1] + 2*areas[2])

print("Part 1: " + str(sum(wrapping)))