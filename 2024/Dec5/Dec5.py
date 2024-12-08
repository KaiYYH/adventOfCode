input = open("Dec5_Input.txt", "r")
import math

rules = []
updates = []
middleValuesCorrect = []
middleValuesIncorrect = []
part1 = 0
part2 = 0

for i in input: 
    if "|" in i: 
        rules.append(i.replace("\n", "").split("|"))
    elif "," in i: 
        updates.append(i.replace("\n", "").split(","))

for update in updates: 
    correct = True
    sorted = False

    while sorted == False: 
        sorted = True
        for rule in rules: 
            if rule[0] in update and rule[1] in update: 
                if(update.index(rule[1]) < update.index(rule[0])): 
                    correct = False
                    sorted = False
                    update.insert(update.index(rule[0]) + 1, rule[1])
                    update.pop(update.index(rule[1]))
        
    if correct == True: 
        middleValuesCorrect.append(update[math.floor(len(update)/2)])
    elif correct == False: 
        middleValuesIncorrect.append(update[math.floor(len(update)/2)])

for n in middleValuesCorrect: 
    part1 += int(n)

for m in middleValuesIncorrect: 
    part2 += int(m)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))