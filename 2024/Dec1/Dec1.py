input = open('Dec1_Input.txt', 'r')

array1 = [] # BOTH
array2 = []
distances = [] # PART 1
sum1 = 0
scores = [] # PART 2
sum2 = 0

for i in input: # INPUT
    split = i.split()
    array1.append(split[0])
    array2.append(split[1])

for num1 in array1: # PART 2
    count = 0
    for num2 in array2: 
        if num1 == num2: 
            count += 1
        
    scores.append(int(num1) * count)

for score in scores: 
    sum2 += int(score)
    
array1.sort() # PART 1
array2.sort()

for num in range(len(array1)): 
    distances.append(abs(int(array1[num]) - int(array2[num])))

for distance in distances: 
    sum1 += distance

print("Part 1: " + str(sum1)) # PART 1
print("Part 2: " + str(sum2)) # PART 2