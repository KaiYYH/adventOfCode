input = open("Dec5Input.txt", "r")

map = [[] for _ in range(7)]
x = -1
for line in input: 
    if "seeds" in line: 
        seeds = line.lstrip("seeds:").split()
    if ("-" not in line) and ("seeds" not in line) and (line != "\n"):  
        map[x].append(line.rstrip("\n").split(" "))
    if "-" in line: 
        x += 1

changed = ["N" for _ in range(len(seeds))]
x = 0
for i in map: 
    for y in i: 
        while x < len(seeds): 
            if int(seeds[x]) < (int(y[1]) + int(y[2])) and (int(seeds[x]) >= int(y[1])) and changed[x] == "N": 
                seeds[x] = int(seeds[x]) - int(y[1]) + int(y[0])
                changed[x] = "Y"
            x += 1
        x = 0
    changed = ["N" for _ in range(len(seeds))]

print(min(seeds))