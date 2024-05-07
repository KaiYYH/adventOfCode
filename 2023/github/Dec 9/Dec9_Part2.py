input = open("Dec9Input.txt", "r")
extrapolated = []

for line in input: 
    current = line.split(" ")
    current = [int(x) for x in current]
    firstValues = []
    zeroSum = 1

    print(current)

    while zeroSum != 0: 
        zeroSum = 0
        temp = []
        i = 0
        while i < len(current) - 1: 
            temp.append(current[i+1] - current[i])
            i += 1
        
        firstValues.append(current[0])
        current = temp

        for n in temp: 
            if n != 0: 
                zeroSum += 1

    sum = 0
    firstValues.reverse()
    for i in firstValues: 
        sum = i - sum
    print(sum)
    extrapolated.append(sum)

total = 0
for n in extrapolated: 
    total += int(n)

print(total)