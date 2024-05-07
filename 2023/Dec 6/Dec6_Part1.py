# reading in file
input = open("Dec6Input.txt", "r")
raceStats = input.readlines()
raceRecords = []

# putting race times in array
raceTime = raceStats[0]
temp = raceTime.rstrip("\n").split(":")
raceTime = temp[1].split()

# putting current records in array
currentRecord = raceStats[1]
temp = currentRecord.split(":")
currentRecord = temp[1].split()

# calculating distance travelled and new records added to array
x = 0 # array index 
while x < len(raceTime): 
    y = 0 # seconds holding down button
    newRecords = 0 # counter for new records
    while y < int(raceTime[x]): 
        distanceTravelled = (int(raceTime[x]) - y) * y

        if distanceTravelled > int(currentRecord[x]): 
            newRecords += 1        
        
        y += 1

    raceRecords.append(newRecords)
    x += 1

# multiplying raceRecords
product = 1 # product of raceRecords items
for i in raceRecords: 
    product *= i

print(product)