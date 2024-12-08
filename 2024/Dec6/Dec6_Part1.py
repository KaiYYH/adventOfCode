input = open("Dec6_Input.txt", "r")

grid = []
count = 0

def next_move(cursor, currentX, currentY): 
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

for i in input: # finding the ^
    grid.append(list(i.replace("\n", "")))
    if "^" in i: 
        currentY = i.index("^")
        line = list(i.replace("\n", ""))

currentX = grid.index(line)
cursor = "^"

while currentX in range(len(grid)) and currentY in range(len(line)): 
    grid[currentX][currentY] = "X"
    
    cursor, currentX, currentY = next_move(cursor, currentX, currentY)

for row in grid: 
    count += row.count("X")

print(count)