input = open("Dec10_Input.txt", "r")

# SETUP
tmap = []
zeros = []
count = 0
count2 = 0

for i in input: 
    tmap.append(list(map(int, list(i.replace("\n", "")))))

# FINDING ZEROS
for x in range(len(tmap)): 
    for y in range(len(tmap[0])): 
        if tmap[x][y] == 0: 
            zeros.append([x, y])

# FUNCTION FOR FINDING NEXT STEP
def next_number(steps, height): 
    if steps[0] - 1 in range(len(tmap)) and tmap[steps[0] - 1][steps[1]] == height + 1: 
        trails[height + 1].append([steps[0] - 1, steps[1]])
    if steps[0] + 1 in range(len(tmap)) and tmap[steps[0] + 1][steps[1]] == height + 1: 
        trails[height + 1].append([steps[0] + 1, steps[1]])
    if steps[1] - 1 in range(len(tmap)) and tmap[steps[0]][steps[1] - 1] == height + 1: 
        trails[height + 1].append([steps[0], steps[1] - 1])
    if steps[1] + 1 in range(len(tmap)) and tmap[steps[0]][steps[1] + 1] == height + 1: 
        trails[height + 1].append([steps[0], steps[1] + 1])

    return trails

# CHECKING ALL THE POSSIBLE TRAILS
for zero in zeros: 
    trails = [ [] for _ in range(10) ]
    trails[0].append(zero)
    for h in range(0, 9): 
        for trail in trails[h]: 
            trails = next_number(trail, h)

    count2 += len(trails[9])

    trailheads = []
    for trailhead in trails[9]: 
        if trailhead not in trailheads: 
            trailheads.append(trailhead)
    
    count += len(trailheads)

print("Part 1: " + str(count))
print("Part 2: " + str(count2))