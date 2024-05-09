input = open('Input4.txt', 'r')

part1 = 0
part2 = 0
ranges = []
for line in input: 
    i = line.rstrip('\n')
    pair = i.split(',')
    for range in pair: 
        ranges.append(range.split('-'))

    # PART 1
    if( (int(ranges[0][0]) <= int(ranges[1][0]) and int(ranges[0][1]) >= int(ranges[1][1])) or (int(ranges[0][0]) >= int(ranges[1][0]) and int(ranges[0][1]) <= int(ranges[1][1])) ): 
        part1 += 1

    # PART 2
    if( (int(ranges[0][0]) <= int(ranges[1][1]) and int(ranges[0][1]) >= int(ranges[1][0])) or (int(ranges[0][0]) >= int(ranges[1][1]) and int(ranges[0][1]) <= int(ranges[1][0])) ): 
        part2 += 1
    ranges = []

# SOLUTIONS
print('Part 1: ', part1)
print('Part 2: ', part2)