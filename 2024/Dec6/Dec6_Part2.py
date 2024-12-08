input = open("Dec6_Input.txt", "r")

grid = []
obstacles = []
count = 0
progress = 0

def next_move(cursor, currentX, currentY): # finds next move to make
    if cursor == "^": 
        if currentX - 1 not in range(len(grid)) or grid[currentX - 1][currentY] != "#": 
            currentX -= 1
        elif grid[currentX - 1][currentY] == "#": 
            cursor = ">"
    elif cursor == ">": 
        if currentY + 1 not in range(len(line)) or grid[currentX][currentY + 1] != "#":
            currentY += 1
        elif grid[currentX][currentY + 1] == "#": 
            cursor = "v"
    elif cursor == "v": 
        if currentX + 1 not in range(len(grid)) or grid[currentX + 1][currentY] != "#": 
            currentX += 1
        elif grid[currentX + 1][currentY] == "#": 
            cursor = "<" 
    elif cursor == "<": 
        if currentY - 1 not in range(len(line)) or grid[currentX][currentY - 1] != "#": 
            currentY -= 1
        elif grid[currentX][currentY - 1] == "#": 
            cursor = "^"

    return (cursor, currentX, currentY)

for i in input: # finding the ^ and setting up the grid
    grid.append(list(i.replace("\n", "")))
    if "^" in i: 
        currentY = i.index("^")
        line = list(i.replace("\n", ""))
currentX = grid.index(line) 
cursor = "^"

while currentX in range(len(grid)) and currentY in range(len(line)): # loop for going through the grid
    cursor, currentX, currentY = next_move(cursor, currentX, currentY)

    if cursor == "^": # puts the obstacle in place
        if currentX - 1 in range(len(grid)) and grid[currentX - 1][currentY] != "#": 
            OX = currentX - 1
            OY = currentY
    elif cursor == ">": 
        if currentY + 1 in range(len(line)) and grid[currentX][currentY + 1] != "#":
            OX = currentX
            OY = currentY + 1
    elif cursor == "v": 
        if currentX + 1 in range(len(grid)) and grid[currentX + 1][currentY] != "#": 
            OX = currentX + 1
            OY = currentY
    elif cursor == "<": 
        if currentY - 1 in range(len(line)) and grid[currentX][currentY - 1] != "#": 
            OX = currentX
            OY = currentY - 1

    holdingCharacter = grid[OX][OY]
    grid[OX][OY] = "#"
    
    print(holdingCharacter)
    originalX = currentX # temporary original variables
    originalY = currentY
    originalCursor = cursor

    obstacleLogged = False

    while originalX in range(len(grid)) and originalY in range(len(line)) and obstacleLogged == False: # loop for going through the grid with the obstacle
        originalCursor, originalX, originalY = next_move(originalCursor, originalX, originalY)
        print("Original: " + str(originalX) + ", " + str(originalY))

        temporaryX = originalX # temporary variables
        temporaryY = originalY
        temporaryCursor = originalCursor

        temporaryCursor, temporaryX, temporaryY = next_move(temporaryCursor, temporaryX, temporaryY) # first move so that original and temporary aren't equal for while loop
        """ print("Original: (" + str(originalX) + ", " + str(originalY) + "), Temporary: (" + str(temporaryX) + ", " + str(temporaryY) + ")") """

        while temporaryX in range(len(grid)) and temporaryY in range(len(line)) and (temporaryX != originalX or temporaryY != originalY): # loop for checking if it has completed a loop
            temporaryCursor, temporaryX, temporaryY = next_move(temporaryCursor, temporaryX, temporaryY)
            """ print("Temporary: " + str(temporaryX) + ", " + str(temporaryY)) """
        
        if temporaryX == originalX and temporaryY == originalY:
            obstacles.append([OX, OY])
            print("Obstacle: " + str(OX) + ", " + str(OY))
            obstacleLogged = True

    grid[OX][OY] = holdingCharacter # removes the obstacle for the next loop

    progress += 1
    print("I've made it through another loop! This is loop: " + str(progress))

print(obstacles)
count = len(obstacles)
print("# of obstacles: " + str(count))
print(grid)