input = open("Dec9_Input.txt", "r")

# VARIABLES
blocks = []
num = 0
checksum = 0

# SETUP
for i in input:
    disk_map = list(i)

for x in range(len(disk_map)): # making blocks
    if x % 2 == 0: 
        for y in range(int(disk_map[x])): 
            blocks.append(num)
        num += 1
    elif x % 2 != 0: 
        for z in range(int(disk_map[x])): 
            blocks.append(".")

# DOING THE THING

next_dot = 0 # initial set
next_num = len(blocks) - 1 # initial value
free_space = 0 # initial set

while next_num >= 0: # stops at the beginning of the array - SHOULD MOVE ON TO THE NEXT SET OF NUMBERS

    next_dot = 0 # start looking for dots from the left again

    while blocks[next_num] == ".": # parsing left to find next numbers to start from
        next_num -= 1

    num_of_nums = 0 # tally of same numbers
    current_num = next_num # position of current check

    while blocks[current_num] == blocks[next_num]: # checking how long this is
        num_of_nums += 1
        current_num -= 1

    print("Number of " + str(blocks[next_num]) + "s: " + str(num_of_nums) + " from index " + str(next_num))

    break_loop = False

    while next_dot < next_num and break_loop == False: # SHOULD CHECK AND MOVE NUMBERS IF SPACE IS AVAILABLE
        while blocks[next_dot] != "." and next_dot < next_num: # parsing right to find next dot for space
            next_dot += 1

        dot_space = 0 # tally of free space
        free_space = next_dot # position of current check

        while blocks[free_space] == ".": # looking for next free space
            dot_space += 1
            if (free_space + 1 < len(blocks) - 1): 
                free_space += 1
            else: 
                break

        print(str(dot_space) + " spaces free from index " + str(next_dot))
        
        if (dot_space >= num_of_nums): # if there is space, shift things around
            for i in range(num_of_nums): 
                blocks[next_dot] = blocks[next_num]
                next_dot += 1

                blocks[next_num] = "."
                next_num -= 1
            break_loop = True # break loop because number has been moved
        else: 
            next_dot = free_space + 1
        
        print("Next dot is " + str(next_dot) + " and next num spot is " + str(next_num) + " with " + str(blocks[next_num]) +  "s")

    next_num = current_num

# ADDING IT ALL UP

for file in range(len(blocks)): # checksum
    if blocks[file] != ".": 
        checksum += file * blocks[file]

print(checksum)