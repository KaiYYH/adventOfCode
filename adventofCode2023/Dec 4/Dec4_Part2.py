gameInput = open("Dec4Input.txt", "r")

# creating card counting array
cardCounter = []
for line in gameInput: 
    cardCounter.append(1)

# body
gameInput = open("Dec4Input.txt", "r")
for line in gameInput: 

    # string manipulation
    singleSpaces = line.replace("  "," ")
    whole = singleSpaces.rstrip(" \n")
    games = whole.split(": ")
    sets = games[1].split(" | ")

    card = games[0].replace(" ", "")
    cardNumber = int(card.lstrip("Card"))

    winningNumbers = sets[0].split(" ")
    numbers = sets[1].split(" ")

    # determining count of matching numbers
    count = 0
    for i in numbers: 
        for j in winningNumbers: 
            if i == j: 
                count += 1

    # edit array of card counter
    index = int(cardNumber) - 1

    x = 1
    while x < count + 1: 
        if (index + x) < 200: 
            cardCounter[index + x] += 1 * cardCounter[index]
        
        x += 1

# sum cardCounter array
sum = 0
for n in cardCounter: 
    sum += int(n)

print(sum)