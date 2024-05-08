input = open('Dec10Input.txt', 'r')

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

# making loop
loop = []
line = []
for i in pipes: 
    for x in pipes[0]:
        line.append('.')
    loop.append(line)
    line = []

x = 0
while x < len(visited): 
    loop[visited[x][0]][visited[x][1]] = pipes[visited[x][0]][visited[x][1]]
    x += 1

finalLoop = []
for i in loop: 
    finalLoop.append(''.join((x) for x in i))

# finding start
pipes = []
for i in finalLoop:     
    pipes.append(i.replace('S', 'F'))

# counting pipes inside loop
total = 0
for row in pipes: 
    counter = 0
    start = ''
    string = row.replace('-', '').replace('FJ', '|').replace('L7', '|')
    for tile in string: 
        if tile in '|FJL7': 
            if start == '': 
                start = tile
                counter = 0
            elif (start == '|') or (tile == '|'): 
                total += counter
                counter = 0
                start = ''
            elif (start == 'L' and tile == 'J') or (start == 'F' and tile == '7'): 
                counter = 0
                start = ''
            else: 
                total += counter
                counter = 0
                start = ''
        else: 
            counter += 1
        
print(total)