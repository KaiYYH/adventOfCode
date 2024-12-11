input = open("Dec7_Input.txt", "r")

calibration = []
sum = 0
sum2 = 0

for i in input: 
    calibration.append(i.replace("\n", "").split(": "))
for set in calibration: 
    set[1] = set[1].split(" ")
for x in calibration: 
    x[0] = int(x[0])
    x[1] = [int(y) for y in x[1]]

def possible(total, values): 
    if len(values) == 1: 
        return total == values[0]
    else: 
        return possible(total, [values[0] + values[1]] + values[2:]) or possible(total, [values[0] * values[1]] + values[2:])

def possible2(total, values): 
    if len(values) == 1: 
        return total == values[0]
    else: 
        return possible2(total, [values[0] + values[1]] + values[2:]) or possible2(total, [values[0] * values[1]] + values[2:]) or possible2(total, [int(str(values[0]) + str(values[1]))] + values[2:])

for line in calibration: 
    if possible(line[0], line[1]): 
        sum += line[0]

    if possible2(line[0], line[1]): 
        sum2 += line[0]

print("Part 1: " + str(sum))
print("Part 2: " + str(sum2))