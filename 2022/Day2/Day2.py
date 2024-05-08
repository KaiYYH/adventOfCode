input = open('Input2.txt', 'r')
data = []
for i in input: 
    data.append(i)

# PART 1
scores = []
score = []
guide = []

def shape(argument): # number for shape
    match argument:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3
        
def rock(argument): # result if rock
    match argument: 
        case 'X': 
            return 3
        case 'Y': 
            return 6
        case 'Z': 
            return 0

def paper(argument): # result if paper
    match argument: 
        case 'X': 
            return 0
        case 'Y': 
            return 3
        case 'Z': 
            return 6
        
def scissors(argument): # result if scissors
    match argument: 
        case 'X': 
            return 6
        case 'Y': 
            return 0
        case 'Z': 
            return 3
        
def result(shape): # number for result
    match shape: 
        case 'A': 
            return rock(guide[1])
        case 'B': 
            return paper(guide[1])
        case 'C': 
            return scissors(guide[1])

for line in data: 
    guide = line.strip('\n').split(' ') # split line into array

    score.append(shape(guide[1]))
    score.append(result(guide[0]))
    scores.append(sum(score)) # append score to array of scores

    guide = [] # reset for new line
    score = [] # reset for new line
part1 = sum(scores)

# PART 2
scores2 = []
def result2(argument): # number for result
    match argument:
        case 'X':
            return 0
        case 'Y':
            return 3
        case 'Z':
            return 6
        
def rock2(argument): # result if rock
    match argument: 
        case 'X': 
            return 3
        case 'Y': 
            return 1
        case 'Z': 
            return 2

def paper2(argument): # result if paper
    match argument: 
        case 'X': 
            return 1
        case 'Y': 
            return 2
        case 'Z': 
            return 3
        
def scissors2(argument): # result if scissors
    match argument: 
        case 'X': 
            return 2
        case 'Y': 
            return 3
        case 'Z': 
            return 1
        
def shape2(shape): # number for result
    match shape: 
        case 'A': 
            return rock2(guide[1])
        case 'B': 
            return paper2(guide[1])
        case 'C': 
            return scissors2(guide[1])

for line in data: 
    guide = line.strip('\n').split(' ') # split line into array

    score.append(result2(guide[1]))
    score.append(shape2(guide[0]))
    scores2.append(sum(score)) # append score to array of scores

    guide = [] # reset for new line
    score = [] # reset for new line
part2 = sum(scores2)

# SOLUTIONS
print('Part 1: ', part1)
print('Part 2: ', part2)