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

    holdingCharacter = grid[OX][OY] # holds character and replaces it with #
    grid[OX][OY] = "#"
    """ if progress == 3:
        print("\n")
        for check in grid: 
            print(check) """
    
    originalX = currentX # temporary original variables
    originalY = currentY
    originalCursor = cursor

    obstacleLogged = False
    looped = 0
    path = []

    while originalX in range(len(grid)) and originalY in range(len(line)) and obstacleLogged == False: # loop for going through the grid with the obstacle
        originalCursor, originalX, originalY = next_move(originalCursor, originalX, originalY)

        if [originalX, originalY, originalCursor] in path: 
            obstacles.append([OX, OY])
            print("Obstacle: " + str(OX) + ", " + str(OY))
            obstacleLogged = True
        else: 
            path.append([originalX, originalY, originalCursor])

    grid[OX][OY] = holdingCharacter # removes the obstacle for the next loop

    progress += 1
    print("I've made it through another loop! This is loop: " + str(progress)) # expect 6093

print(obstacles) # counting obstacles

unique_obstacles = []

for obstacle in obstacles: 
    if obstacle not in unique_obstacles:
        unique_obstacles.append(obstacle)

count = len(unique_obstacles)
print("# of obstacles: " + str(count))

# 2422 is too high
# 2249 is too high