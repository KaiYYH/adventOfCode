input = open("Dec9_Input.txt", "r")

blocks = []
num = 0
checksum = 0

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

def remove_dots(array): # removing dots if they are at the end
    if(array[-1]) == ".": 
        array = array[:-1]
        array = remove_dots(array)

    return array

numbers = 0 # how many times it should go through the loop
for num in blocks: 
    if num != ".": 
        numbers += 1

for block in range(numbers): # re-arranging
    blocks = remove_dots(blocks)

    if blocks[block] == ".": 
        blocks[block] = blocks[-1]
        blocks = blocks[:-1]

blocks = remove_dots(blocks)

print(blocks)

for file in range(len(blocks)): # checksum
    checksum += file * blocks[file]

print(checksum)