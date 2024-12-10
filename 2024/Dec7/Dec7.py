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
    print(str(total) + ": " + str(values))
    if len(values) == 1: 
        return total == values[0]

    if total >= values[0] * values[1]:
        multiplied = values
        multiplied[1] = multiplied[0] * multiplied[1]
        multiplied = multiplied[1:]

        if possible(total, multiplied):
            return True
    
    if total >= values[0] + values[1]: 
        added = values
        added[1] = added[0] + added[1]
        added = added[1:]
        
        if possible(total, added):
            return True
    
    return False

def possible2(total, values): 
    """ print(str(total) + ": " + str(values)) """
    if len(values) == 1: 
        return total == values[0]
    
    if total % values[0] == 0 and possible2(total // values[0], values[1:]): 
        """ print(str(total) + ": " + str(values)) """
        return True
    if total - values[0] >= 0 and possible2(total - values[0], values[1:]): 
        """ print(str(total) + ": " + str(values)) """
        return True
    
    if total <= int(str(values[0]) + str(values[1])):
        values[1] = int(str(values[0]) + str(values[1]))
        values = values[1:]
    
        if possible2(total, values): 
            return True

    return False

for line in calibration: 
    if possible(line[0], line[1]): 
        sum += line[0]

    if possible2(line[0], line[1]): 
        sum2 += line[0]

print("Part 1: " + str(sum)) # should be 3749
print("Part 2: " + str(sum2)) # 1584061710088 is too low