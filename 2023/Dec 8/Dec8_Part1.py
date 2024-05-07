file = open("Dec8Input.txt", "r")
lines = file.readlines()
key = []
left = []
right = []
looking = "AAA"
x = 0
count = 0

# reading file into arrays
guide = lines[0].rstrip("\n")
for i in lines[2:]: 
    temp = i.rstrip("\n")
    temp1 = temp.replace("(", "")
    temp2 = temp1.replace(")", "")
    temp3 = temp2.split(" = ")
    key.append(temp3[0])
    temp4 = temp3[1].split(", ")
    left.append(temp4[0])
    right.append(temp4[1])

while looking != "ZZZ": 
    index = key.index(looking)
    if guide[x] == "R": 
        looking = right[index]
    elif guide[x] == "L": 
        looking = left[index]

    if x < len(guide) - 1:
        x += 1
    elif x == len(guide) - 1: 
        x = 0
    count += 1

print(count)