file = open("Dec7Input.txt", "r")
from collections import Counter
temp = []
hands = []
ranked = []
list = {}
total = 0
highest = 0

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
strength = "AKQT98765432J"

# ranking function
def rank(count, hand, highest): 

    # altering for jokers
    if 'J' in hand: 
        if count != 1: 
            count -= 1
        if hands[0][0] != 'J':
            highest += hand.count('J')
        else:
            try: 
                highest += hands[1][1]
            except IndexError:
                pass 

    if count == 5:
        types.setdefault("High card", []).append(hand)
    elif count == 4:
        types.setdefault("One pair", []).append(hand)
    elif count == 3:
        if highest == 3:
            types.setdefault("Three of a kind", []).append(hand)
        else:
            types.setdefault("Two pair", []).append(hand)
    elif count == 2:
        if highest == 3:
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
    hands = sorted(count.items(), key=lambda index: (index[1], index[0]))
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
for i in ranked: 
    total += (highest + 1) * int(list[i])
    highest +=1

print(total)