input = open("Dec4_Input.txt", "r")

grid = []
xmas = "MMASS"
count = 0
orientations = [
                [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]], 
                [[0, 0], [2, 0], [1, 1], [0, 2], [2, 2]], 
                [[0, 0], [2, 0], [1, -1], [0, -2], [2, -2]], 
                [[0, 0], [0, 2], [-1, 1], [-2, 0], [-2, 2]]]

for i in input: 
    grid.append(i.replace("\n", ""))

for orientation in orientations: 
    for row in range(len(grid)): 
        for character in range(len(grid[0])): 
            position = 0
            
            for letter in xmas: 
                x = row + orientation[position][0]
                y = character + orientation[position][1]

                if x not in range(len(grid)) or y not in range(len(grid[0])) or grid[x][y] != letter:
                    break
                    
                if position == len(xmas) - 1: 
                    count += 1

                position += 1

print("Part 2: " + str(count))