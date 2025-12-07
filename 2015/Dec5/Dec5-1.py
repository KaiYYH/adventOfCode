input, nice = open("Dec5.txt", "r"), 0

def vowels(string): 
    return string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u') >= 3

def twice(string): 
    for char in range(len(string) - 1):
        if string[char] == string[char + 1]:
            return True
    return False

def contains(string): 
    return "ab" not in string and "cd" not in string and "pq" not in string and "xy" not in string

for i in input: 
    if vowels(i) == True and twice(i) == True and contains(i) == True: 
        nice += 1

print("Part 1: " + str(nice))