input = open('Input3.txt', 'r')
data = []
for i in input: 
    data.append(i)

priorities = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

# PART 1
firstHalf = ''
secondHalf = ''
common = ''
part1 = 0

for line in data: 
    i = line.rstrip('\n')
    firstHalf = set(i[0:len(i)//2])
    secondHalf = set(i[len(i)//2:])

    commmonCharacters = list(set([char for char in firstHalf if char in secondHalf])) 
    for char in commmonCharacters: 
        part1 += priorities[char]

    firstHalf = ''
    secondHalf = ''
    common = ''

# PART 2
group = []
commonChars = []
part2 = 0

for line in data: 
    i = line.rstrip('\n')
    group.append(i)
    
    if len(group) == 3: 
        for char in group[0]: 
            if char in group[1] and char in group[2]: 
                commonChars.append(char)
                break
        group = []
    
for char in commonChars: 
    part2 += priorities[char]

# SOLUTIONS
print('Part 1: ', part1)
print('Part 2: ', part2)