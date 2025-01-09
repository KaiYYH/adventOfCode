import math
import re

input = open("Dec14_Input.txt", "r")
data = []
grid = [101, 103] # length, height
seconds_elapsed = 100
final_positions = []
q = [0 for i in range(4)]

for line in input: 
    data.append(re.split(r"[ =,pv\n]", line))

def final_position(data, grid, seconds_elapsed):
    x = ((int(data[2]) + 1) + (int(data[6]) * seconds_elapsed)) % grid[0]
    y = ((int(data[3]) + 1) + (int(data[7]) * seconds_elapsed)) % grid[1] 

    if x == 0: 
        x = grid[0]
    if y == 0: 
        y = grid[1]
    
    return [x, y]

for i in range(len(data)): 
    final_positions.append(final_position(data[i], grid, seconds_elapsed))

for position in final_positions: 
    if(position[0] < math.ceil(grid[0] / 2)) and (position[1] < math.ceil(grid[1] / 2)): 
        q[0] += 1
    elif(position[0] < math.ceil(grid[0] / 2)) and (position[1] > math.ceil(grid[1] / 2)): 
        q[1] += 1
    elif(position[0] > math.ceil(grid[0] / 2)) and (position[1] < math.ceil(grid[1] / 2)): 
        q[2] += 1
    elif(position[0] > math.ceil(grid[0] / 2)) and (position[1] > math.ceil(grid[1] / 2)): 
        q[3] += 1

print(q[0] * q[1] * q[2] * q[3])