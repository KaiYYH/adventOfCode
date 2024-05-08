gameInput = open("Day4Input.txt", "r")

counter = 0

for line in gameInput: 

    singleSpaces = line.replace("  "," ")
    whole = singleSpaces.rstrip(" \n")
    games = whole.split(": ")
    sets = games[1].split(" | ")

    winningNumbers = sets[0].split(" ")
    numbers = sets[1].split(" ")

    count = 0

    for i in numbers: 

        for j in winningNumbers: 

            if i == j: 

                if count == 0: 
                    count = 1
                else: 
                    count *= 2

    counter += count

print(counter)