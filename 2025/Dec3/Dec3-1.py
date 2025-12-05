input, Part1 = open("Dec3Input.txt", "r"), 0

def highest(num):
    largest = 0
    while (num):
        current = num % 10
        largest = max(current, largest)
        num = num // 10

    return largest

for i in input: 
    first = highest((int(i) // 10))
    second = highest(int(i[i.find(str(first)) + 1:]))
    Part1 += int(str(first) + str(second))

print("Part1: " + str(Part1))