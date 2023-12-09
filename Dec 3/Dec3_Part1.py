input = open("Dec3Input.txt", "r")

current = []
partNumbers = []

engineSchematic = input.readlines()

print(engineSchematic)

'''# current array loop
for line in engineSchematic: 
    string = line.rstrip("\n")
    nextrow = []
    nextrow.extend(string)

    print(nextrow)

    # checking if numeric and adding to partNumbers array
    i = 0
    symbols = 0
    string = ""

    while i < len(current): 
        # checking if current item is numeric
        if current[i].isnumeric() == True: 
            string = string + current[i]

            # checking for symbols
            if lastrow[i-1].isnumeric == False and lastrow[i-1] != ".": 
                symbols += 1
            elif lastrow[i].isnumeric == False and lastrow[i] != ".": 
                symbols += 1
            elif lastrow[i+1].isnumeric == False and lastrow[i+1] != ".": 
                symbols += 1
            elif current[i-1].isnumeric == False and current[i-1] != ".": 
                symbols += 1
            elif current[i+1].isnumeric == False and current[i+1] != ".": 
                symbols += 1
            elif nextrow[i-1].isnumeric == False and nextrow[i-1] != ".": 
                symbols += 1
            elif nextrow[i].isnumeric == False and nextrow[i] != ".": 
                symbols += 1
            elif nextrow[i+1].isnumeric == False and nextrow[i+1] != ".": 
                symbols += 1

            # checking if next item is numeric
            if current[i+1].isnumeric() == False:
                if symbols == 0: 
                    partNumbers.append(string)
                
                string = ""
                symbols = 0
        
        i += 1 

    # shifting reference arrays
    lastrow = current
    current = nextrow'''


'''# sum partNumbers array
sum = 0
for n in partNumbers: 
    sum += int(n)

print(sum)'''