input = open('Dec10InputTest5.txt', 'r')

# finding start
x = 0
pipes = []
for i in input: 
    pipes.append(i.rstrip('\n'))
    if 'S' in i: 
        startcol = i.index('S')
        startrow = x
    x += 1

# first step S - assumes first step is to the right
lastrow = startrow
lastcol = startcol
row = startrow
col = startcol + 1
visited = [[startrow, startcol]]

# loop with pipes
count = 1
while pipes[row][col] != 'S':
    visited.append([row, col])
    if pipes[row][col] == '|':
        if row > lastrow:
            lastrow = row
            lastcol = col
            row += 1
        elif row < lastrow: 
            lastrow = row
            lastcol = col
            row -= 1
    elif pipes[row][col] == '-':
        if col > lastcol: 
            lastrow = row
            lastcol = col
            col += 1
        elif col < lastcol: 
            lastrow = row
            lastcol = col
            col -= 1
    elif pipes[row][col] == 'L':
        if col == lastcol: 
            lastrow = row
            lastcol = col
            col += 1
        elif row == lastrow: 
            lastrow = row
            lastcol = col
            row -= 1
    elif pipes[row][col] == 'J':
        if col == lastcol: 
            lastrow = row
            lastcol = col
            col -= 1
        elif row == lastrow: 
            lastrow = row
            lastcol = col
            row -= 1
    elif pipes[row][col] == 'F':
        if col == lastcol: 
            lastrow = row
            lastcol = col
            col += 1
        elif row == lastrow: 
            lastrow = row
            lastcol = col
            row += 1
    elif pipes[row][col] == '7':
        if col == lastcol: 
            lastrow = row
            lastcol = col
            col -= 1
        elif row == lastrow: 
            lastrow = row
            lastcol = col
            row += 1

    count += 1
    
# print counter
print(visited)
print(int(count/2))