input = open('Input1.txt', 'r')

# PART 1
sums = [] # keep sum of each elf
elf = 0 # temporary to add up each elf's calories
for i in input: 
    if i == '\n': 
        sums.append(elf) # appends sum to sums array
        elf = 0 # resets for new elf
    else: 
        elf += int(i.rstrip('\n')) # adds value to sum of current elf
sums.append(elf) # append last sum to sums array
part1 = max(sums)

# PART 2
top = [] # to keep the top three
for i in range(3): 
    top.append(max(sums)) # appends top sum to top three array
    sums.remove(max(sums)) # removes top sum from sums array
part2 = sum(top)

# SOLUTIONS
print('Part 1: ', part1)
print('Part 2: ', part2)