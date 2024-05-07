with open("Dec15Input.txt") as input:
    file = input.read()
initSeq = file.split(",")

# dictionary
ASCII = {
    45: "-", 48: "0", 49: "1", 50: "2", 51: "3", 52: "4", 53: "5", 54: "6", 55: "7", 56: "8", 57: "9", 61: "=", 65: "A", 66: "B", 
    67: "C", 68: "D", 69: "E", 70: "F", 71: "G", 72: "H", 73: "I", 74: "J", 75: "K", 76: "L", 77: "M", 78: "N", 79: "O", 80: "P", 
    81: "Q", 82: "R", 83: "S", 84: "T", 85: "U", 86: "V", 87: "W", 88: "X", 89: "Y", 90: "Z", 97: "a", 98: "b", 99: "c", 100: "d", 
    101: "e", 102: "f", 103: "g", 104: "h", 105: "i", 106: "j", 107: "k", 108: "l", 109: "m", 110: "n", 111: "o", 112: "p", 113: "q", 
    114: "r", 115: "s", 116: "t", 117: "u", 118: "v", 119: "w", 120: "x", 121: "y", 122: "z"
}

# dictionary searcher function
def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k
    return None

# HASH function
def HASH(string): 
    current = 0
    if "-" in string: 
        string = string.split("-")
    elif "=" in string: 
        string = string.split("=")
    for i in string[0]: 
        current += search(ASCII, i)
        current *= 17
        current %= 256
    return current

# boxes
boxes = [[] for _ in range(256)]
for i in initSeq: 
    box = HASH(i) # 
    if "=" in i: 
        look = i.split("=")
        if any(look[0] in s for s in boxes[box]):
            for x in boxes[box]: 
                if look[0] in x: 
                    index = boxes[box].index(x) 
            boxes[box][index] = i
        else: 
            boxes[box].append(i)
    if "-" in i: 
        look = i.split("-")
        if any(look[0] in s for s in boxes[box]): 
            for x in boxes[box]: 
                if look[0] in x: 
                    index = boxes[box].index(x) 
            boxes[box].remove(boxes[box][index])

# calculation
power = []
for box in boxes: 
    for lens in box: 
        if "-" in lens: 
            length = lens.split("-")
        elif "=" in lens: 
            length = lens.split("=")
        power.append((boxes.index(box) + 1) * (box.index(lens) + 1) * int(length[1]))

# total
total = sum(power)
print(total)