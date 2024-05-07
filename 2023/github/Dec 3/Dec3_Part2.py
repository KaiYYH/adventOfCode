# reading input and variables
input = open("Dec3Input.txt", "r")
engineSchematic = []
adjacentNums = []
gearRatios = []
num = ""

# loops
for i in input: 
    engineSchematic.append(i.rstrip("\n"))

# adding padding
line = 0
while line < len(engineSchematic): 
    engineSchematic[line] = "." + engineSchematic[line] + "."
    line += 1

x = 0
y = 0
while x < len(engineSchematic): 
    y = 0
    while y < len(engineSchematic): 
        if engineSchematic[x][y] == "*": 
            if engineSchematic[x][y - 1].isnumeric() == True: # left
                index = y - 1
                while engineSchematic[x][index].isnumeric() == True: 
                    num = engineSchematic[x][index] + num
                    index -= 1
                adjacentNums.append(num)
                num = ""
            if engineSchematic[x][y + 1].isnumeric() == True: # right
                index = y + 1
                while engineSchematic[x][index].isnumeric() == True: 
                    num = num + engineSchematic[x][index]
                    index += 1
                adjacentNums.append(num)
                num = ""
            # above
            above = engineSchematic[x - 1][y - 1] + engineSchematic[x - 1][y] + engineSchematic[x - 1][y + 1]
            if engineSchematic[x - 1][y - 1].isnumeric() == True: # adding left into above string
                index = y - 2
                while engineSchematic[x - 1][index].isnumeric() == True: 
                    above = engineSchematic[x - 1][index] + above
                    index -= 1
            if engineSchematic[x - 1][y + 1].isnumeric() == True: # adding right into above string
                index = y + 2
                while engineSchematic[x - 1][index].isnumeric() == True: 
                    above = above + engineSchematic[x - 1][index]
                    index += 1
            above = above + "." # padding on the end of above string
            for i in above: # adding above numbers to adjacent numbers array
                if i.isnumeric() == True: 
                    num = num + i
                else: 
                    if num != "": 
                        adjacentNums.append(num)
                        num = ""
            # below
            below = engineSchematic[x + 1][y - 1] + engineSchematic[x + 1][y] + engineSchematic[x + 1][y + 1]
            if engineSchematic[x + 1][y - 1].isnumeric() == True: # adding left into below string
                index = y - 2
                while engineSchematic[x + 1][index].isnumeric() == True: 
                    below = engineSchematic[x + 1][index] + below
                    index -= 1
            if engineSchematic[x + 1][y + 1].isnumeric() == True: # adding right into below string
                index = y + 2
                while engineSchematic[x + 1][index].isnumeric() == True: 
                    below = below + engineSchematic[x + 1][index]
                    index += 1
            below = below + "." # padding on the end of below string
            for i in below: # adding below numbers to adjacent numbers array
                if i.isnumeric() == True: 
                    num = num + i
                else: 
                    if num != "": 
                        adjacentNums.append(num)
                        num = ""
        y += 1
        print(adjacentNums)
        if len(adjacentNums) == 2: 
            product = int(adjacentNums[0]) * int(adjacentNums[1])
            gearRatios.append(product)
        adjacentNums = []
    x += 1

# sum gear ratios
total = sum(gearRatios)
print(total)