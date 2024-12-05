input = open("Dec4_Input.txt", "r")

grid = []
xmas = "XMAS"
count = 0
directions = [[0, 1], [1, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [1, -1], [-1, 1]]

for i in input: 
    grid.append(i.replace("\n", ""))

for direction in directions: 
    for row in range(len(grid)): 
        for character in range(len(grid[0])): 
            x = row
            y = character

            for letter in xmas: 
                if x not in range(len(grid)) or y not in range(len(grid[0])) or grid[x][y] != letter:
                    break

                if letter == "S": 
                    count += 1

                x += int(direction[0])
                y += int(direction[1])

print("Part 1: " + str(count))