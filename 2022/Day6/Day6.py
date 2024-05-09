input = open('Input6.txt', 'r')

def unique(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)): 
            if(str[i] == str[j]):
                return False
    return True

def marker(string, requiredCharacters): 
    substring = 'xx'
    x = 0

    while unique(substring) == False:  
        substring = string[x: x + requiredCharacters]
        print(substring)
        x += 1

    return x + requiredCharacters - 1

for line in input: 
    part1 = marker(line, 4)
    part2 = marker(line, 14)

# SOLUTIONS
print('Part 1: ', part1)
print('Part 2: ', part2)