input = open("Dec1.txt", "r")
previous = ""
increases = 0

for data in input: 

    if isinstance(previous, int) and previous < int(data): 
        increases += 1
    
    previous = int(data)

print(increases)