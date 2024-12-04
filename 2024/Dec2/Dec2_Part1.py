input = open('Dec2_Input.txt', 'r')

count = 0

for line in input: 
    row = line.split()
    first = row[0]
    second = row[1]
    safe = True

    difference = int(first) - int(second)

    for i in range(1, len(row)):
        second = row[i]
        if abs(int(first) - int(second)) > 3: 
            safe = False
        elif (difference * (int(first) - int(second))) < 0: 
            safe = False
        elif first == second: 
            safe = False

        difference = int(first) - int(second)
        first = row[i]
        
    if safe == True: 
        count += 1

print("Part 1: " + str(count))