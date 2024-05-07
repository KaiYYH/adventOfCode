file = open("Dec7Input.txt", "r")
from collections import Counter
temp = []
hands = []
ranked = []
list = {}

# hand information
types = {
    "Five of a kind": [],
    "Four of a kind": [],
    "Full house": [],
    "Three of a kind": [],
    "Two pair": [],
    "One pair": [],
    "High card": []
}
strength = "AKQJT98765432"

# ranking function
def rank(x, hand, y): 
    if x == 5:
        types.setdefault("High card", []).append(hand)
    elif x == 4:
        types.setdefault("One pair", []).append(hand)
    elif x == 3:
        if y == 3:
            types.setdefault("Three of a kind", []).append(hand)
        else:
            types.setdefault("Two pair", []).append(hand)
    elif x == 2:
        if y == 3:
            types.setdefault("Full house", []).append(hand)
        else:
            types.setdefault("Four of a kind", []).append(hand)
    else:
        types.setdefault("Five of a kind", []).append(hand)

# reading file into dictionary
for line in file:
    line = line.rstrip("\n")
    temp.append(line)

for i in temp:
    list[i.split(' ')[0]] = i.split(' ')[1]
hands = list.keys()

# ranking array
for hand in hands:
    # sorting
    count = Counter(hand)
    hands = sorted(count.items(), key=lambda index: index[1])
    hands.reverse()

    # ranking
    rank(len(hands), hand, hands[0][1])

# sorting
for key, value in types.items():
    types[key] = sorted(value, key=lambda cards: [strength.index(card[0]) for card in cards])

# fully ranked
for key, value in types.items():
    ranked += value
ranked.reverse()

# total
total = 0
y = 0
for i in ranked: 
    total += (y + 1) * int(list[i])
    y +=1

print(total)