# reading input and variables
input = open("Dec3Input.txt", "r")
engineSchematic = []
numbers = []
string = ""

# loops
for i in input: 
    engineSchematic.append(i.rstrip("\n"))

x = 0
while x < len(engineSchematic): 
    i = 0
    symbols = 0
    while i < len(engineSchematic[x]): 
        if engineSchematic[x][i].isnumeric() == True:
            string = string + engineSchematic[x][i]

            # checking if it is a valid number
            if x == 0: 
                if i == 0: 
                    if engineSchematic[x][i+1].isnumeric() == False and engineSchematic[x][i+1] != ".": 
                        symbols += 1
                    if engineSchematic[x+1][i].isnumeric() == False and engineSchematic[x+1][i] != ".": 
                        symbols += 1
                    if engineSchematic[x+1][i+1].isnumeric() == False and engineSchematic[x+1][i+1] != ".": 
                        symbols += 1
                elif i == len(engineSchematic[x]) - 1: 
                    if engineSchematic[x][i-1].isnumeric() == False and engineSchematic[x][i-1] != ".": 
                        symbols += 1
                    if engineSchematic[x+1][i-1].isnumeric() == False and engineSchematic[x+1][i-1] != ".": 
                        symbols += 1
                    if engineSchematic[x+1][i].isnumeric() == False and engineSchematic[x+1][i] != ".": 
                        symbols += 1
                else: 
                    if engineSchematic[x][i-1].isnumeric() == False and engineSchematic[x][i-1] != ".": 
                        symbols += 1
                    if engineSchematic[x][i+1].isnumeric() == False and engineSchematic[x][i+1] != ".": 
                        symbols += 1
                    if engineSchematic[x+1][i-1].isnumeric() == False and engineSchematic[x+1][i-1] != ".": 
                        symbols += 1
                    if engineSchematic[x+1][i].isnumeric() == False and engineSchematic[x+1][i] != ".": 
                        symbols += 1
                    if engineSchematic[x+1][i+1].isnumeric() == False and engineSchematic[x+1][i+1] != ".": 
                        symbols += 1
            elif x == len(engineSchematic) - 1: 
                if i == 0: 
                    if engineSchematic[x][i+1].isnumeric() == False and engineSchematic[x][i+1] != ".": 
                        symbols += 1
                    if engineSchematic[x-1][i].isnumeric() == False and engineSchematic[x-1][i] != ".": 
                        symbols += 1
                    if engineSchematic[x-1][i+1].isnumeric() == False and engineSchematic[x-1][i+1] != ".": 
                        symbols += 1
                elif i == len(engineSchematic[x]) - 1: 
                    if engineSchematic[x][i-1].isnumeric() == False and engineSchematic[x][i-1] != ".": 
                        symbols += 1
                    if engineSchematic[x-1][i-1].isnumeric() == False and engineSchematic[x-1][i-1] != ".": 
                        symbols += 1
                    if engineSchematic[x-1][i].isnumeric() == False and engineSchematic[x-1][i] != ".": 
                        symbols += 1
                else: 
                    if engineSchematic[x][i-1].isnumeric() == False and engineSchematic[x][i-1] != ".": 
                        symbols += 1
                    if engineSchematic[x][i+1].isnumeric() == False and engineSchematic[x][i+1] != ".": 
                        symbols += 1
                    if engineSchematic[x-1][i-1].isnumeric() == False and engineSchematic[x-1][i-1] != ".": 
                        symbols += 1
                    if engineSchematic[x-1][i].isnumeric() == False and engineSchematic[x-1][i] != ".": 
                        symbols += 1
                    if engineSchematic[x-1][i+1].isnumeric() == False and engineSchematic[x-1][i+1] != ".": 
                        symbols += 1
            else: 
                if i == 0: 
                    if engineSchematic[x][i+1].isnumeric() == False and engineSchematic[x][i+1] != ".": 
                        symbols += 1
                    if engineSchematic[x-1][i].isnumeric() == False and engineSchematic[x-1][i] != ".": 
                        symbols += 1
                    if engineSchematic[x-1][i+1].isnumeric() == False and engineSchematic[x-1][i+1] != ".": 
                        symbols += 1
                    if engineSchematic[x+1][i].isnumeric() == False and engineSchematic[x+1][i] != ".": 
                        symbols += 1
                    if engineSchematic[x+1][i+1].isnumeric() == False and engineSchematic[x+1][i+1] != ".": 
                        symbols += 1
                elif i == len(engineSchematic[x]) - 1: 
                    if engineSchematic[x][i-1].isnumeric() == False and engineSchematic[x][i-1] != ".": 
                        symbols += 1
                    if engineSchematic[x-1][i-1].isnumeric() == False and engineSchematic[x-1][i-1] != ".": 
                        symbols += 1
                    if engineSchematic[x-1][i].isnumeric() == False and engineSchematic[x-1][i] != ".": 
                        symbols += 1
                    if engineSchematic[x+1][i-1].isnumeric() == False and engineSchematic[x+1][i-1] != ".": 
                        symbols += 1
                    if engineSchematic[x+1][i].isnumeric() == False and engineSchematic[x+1][i] != ".": 
                        symbols += 1
                else: 
                    if engineSchematic[x][i-1].isnumeric() == False and engineSchematic[x][i-1] != ".": 
                        symbols += 1
                    if engineSchematic[x][i+1].isnumeric() == False and engineSchematic[x][i+1] != ".": 
                        symbols += 1
                    if engineSchematic[x-1][i-1].isnumeric() == False and engineSchematic[x-1][i-1] != ".": 
                        symbols += 1
                    if engineSchematic[x-1][i].isnumeric() == False and engineSchematic[x-1][i] != ".": 
                        symbols += 1
                    if engineSchematic[x-1][i+1].isnumeric() == False and engineSchematic[x-1][i+1] != ".": 
                        symbols += 1
                    if engineSchematic[x+1][i-1].isnumeric() == False and engineSchematic[x+1][i-1] != ".": 
                        symbols += 1
                    if engineSchematic[x+1][i].isnumeric() == False and engineSchematic[x+1][i] != ".": 
                        symbols += 1
                    if engineSchematic[x+1][i+1].isnumeric() == False and engineSchematic[x+1][i+1] != ".": 
                        symbols += 1

            # check if it's the last digit in the number
            if i == len(engineSchematic[x]) - 1: 
                if symbols > 0:  
                    numbers.append(string)
                string = ""
                symbols = 0
            elif engineSchematic[x][i+1].isnumeric() == False:
                if symbols > 0:  
                    numbers.append(string)
                string = ""
                symbols = 0
        i += 1
    x += 1

print(numbers) # PRINTING NUMBERS ARRAY

# sum numbers array
sum = 0
for n in numbers: 
    sum += int(n)
print(sum)