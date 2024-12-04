import re
input = open('Dec3_Input.txt', 'r')

sum = 0
muls = 0
enabled = True

for line in input: 
    string = line

    pairs = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", string)

    for i in pairs: 
        if enabled == True: 
            if i[3] == "don't()": 
                enabled = False
            elif i[2] == "": 
                sum += int(i[0]) * int(i[1])
                muls += 1
        elif enabled == False: 
            if i[2] == "do()": 
                enabled = True
            elif i[3] == "": 
                muls += 1

print("Part 2: " + str(sum))