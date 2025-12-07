input, nice = open("Dec5.txt", "r"), 0

def pairs(string): 
    for char in range(len(string) - 3): 
        if string[char:char + 2] in string[char + 2:]: 
            return True
    return False

def sandwich(string): 
    for char in range(len(string) - 2):
        if string[char] == string[char + 2]:
            return True
    return False

for i in input: 
    if pairs(i) == True and sandwich(i) == True: 
        nice += 1

print("Part 2: " + str(nice))