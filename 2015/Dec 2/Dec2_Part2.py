input = open("Dec2Input.txt", "r")
ribbon = []

for i in input: 
    dimensions = i.split("x")
    additions = [int(dimensions[0])+int(dimensions[1]), int(dimensions[1])+int(dimensions[2]), int(dimensions[0])+int(dimensions[2])]
    ribbon.append(2*min(additions) + int(dimensions[0])*int(dimensions[1])*int(dimensions[2]))

print("Part 2: " + str(sum(ribbon)))