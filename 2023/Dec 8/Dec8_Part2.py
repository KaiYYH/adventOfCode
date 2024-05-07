file = open("Dec8Input.txt", "r")
import math
lines = file.readlines()
key = []
left = []
right = []
looking = []
x = 0
count = 1
notZ = 1

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

# finding ones that end in A
for i in key: 
    if i[2] == "A": 
        looking.append(i)

print(guide)
print(looking)

while notZ > 0: 
    notZ = 0
    for i in range(len(looking)): 
        if type(looking[i]) == str:
            index = key.index(looking[i])
            if guide[x] == "R": 
                looking[i] = right[index]
            elif guide[x] == "L": 
                looking[i] = left[index]

        if type(looking[i]) == int: 
            continue
        elif looking[i][2] == "Z": 
            looking[i] = count
        else: 
            notZ += 1

    if x < len(guide) - 1:
        x += 1
    elif x == len(guide) - 1: 
        x = 0

    print(x) #REMOVE
    print(looking)
    count += 1

# calculate lcm
def lcm(a,b):
  return (a * b) // math.gcd(a,b)
x = 0
steps = 1

for i in looking: 
    steps = lcm(i, steps)

print(steps) 