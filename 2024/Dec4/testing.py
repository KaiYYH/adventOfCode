input = open("Dec4_Input.txt", "r")

count = 0

for i in input: 
    for x in i: 
        if x == "X": 
            count += 1

print(count)