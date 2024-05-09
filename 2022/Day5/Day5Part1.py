input = open('Input5.txt', 'r')
data = []
for i in input: 
    data.append(i)

crates = [ [], [], [], [], [], [], [], [], []] 
instructions = [] # quantity, from, to
part1 = ''

for line in data: # separating file data
    if '[' in line: 
        crates[0].insert(0, line[1])
        crates[1].insert(0, line[5])
        crates[2].insert(0, line[9])
        crates[3].insert(0, line[13])
        crates[4].insert(0, line[17])
        crates[5].insert(0, line[21])
        crates[6].insert(0, line[25])
        crates[7].insert(0, line[29])
        crates[8].insert(0, line[33])

    if 'move' in line: 
        instructions.append(line.rstrip('\n').replace('move ', '').replace(' from ', ' ').replace(' to ', ' ').split(' '))

def removeBlanks(crates): # removing blanks from crates
    for crate in crates: 
        while ' ' in crate: 
            crate.remove(' ')
removeBlanks(crates)

modifiedCrates = crates
for x in instructions: 
    for y in range(int(x[0])):
        modifiedCrates[int(x[2]) - 1].append(modifiedCrates[int(x[1]) - 1][len(modifiedCrates[int(x[1]) - 1]) - 1])
        modifiedCrates[int(x[1]) - 1].pop()

for crate in modifiedCrates: 
    part1 = part1 + crate[len(crate) - 1]

# SOLUTION
print('Part 1: ', part1)