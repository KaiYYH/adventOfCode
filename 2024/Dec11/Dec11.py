input = open("Dec11_Input.txt", "r")

for i in input: 
    stones_list = list(map(int, i.split(" ")))

def blink(stones): 
    stone = 0

    while stone < len(stones): 
        if stones[stone] == 0: 
            stones[stone] = 1
        elif len(str(stones[stone])) % 2 == 0: 
            string = str(stones[stone])
            stones[stone] = int(string[:len(string)//2])
            stones.insert(stone + 1, int(string[len(string)//2:]))
            stone += 1
        else: 
            stones[stone] *= 2024
        
        stone += 1
    
    return stones

for i in range(25): 
    stones_list = blink(stones_list)
    print("Blink #: " + str(i))

print(len(stones_list))

for j in range(50): 
    stones_list = blink(stones_list)
    print("Blink #: " + str(j))

print(len(stones_list))