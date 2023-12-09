# reading in file
input = open("Dec6Input.txt", "r")
raceStats = input.readlines()
raceRecords = []

# putting race times in array
raceTime = raceStats[0]
temp = raceTime.rstrip("\n").split(":")
raceTime = temp[1].replace(" ", "")

# putting current records in array
currentRecord = raceStats[1]
temp = currentRecord.split(":")
currentRecord = temp[1].replace(" ", "")

# calculating distance travelled and new records added to array
y = 0 # seconds holding down button
newRecords = 0 # counter for new records
while y < int(raceTime): 
    distanceTravelled = (int(raceTime) - y) * y

    if distanceTravelled > int(currentRecord): 
        newRecords += 1        
    
    y += 1

print(newRecords)