input = open("Dec11_Input.txt", "r")

for i in input: 
    stones_list = list(map(int, i.split(" ")))

twenty_five = 0
seventy_five = 0

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

for stone in stones_list: 
    initial = [stone]
    for i in range(25): 
        initial = blink(initial)

        twenty_five += len(initial)
        seventy_five += len(initial)

        print("Blink #: " + str(i))

    for j in range(50): 
        initial = blink(initial)

        seventy_five += len(initial)

        print("Blink #: " + str(25 + j))
    
    print("Onto the " + str(stone) + " stone")

print("Part 1: " + str(twenty_five))
print("Part 2: " + str(seventy_five))