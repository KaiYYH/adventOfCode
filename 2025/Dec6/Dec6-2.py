input, worksheet, cephalopod, operation, total, sum = open("Dec6.txt", "r"), [], [], "", 0, 0

for i in input: 
    worksheet.append(list(i.replace("\n", "")))

worksheet = [[worksheet[j][i] for j in range(len(worksheet))] for i in range(len(worksheet[0]))]

for list in worksheet: 
    cephalopod .append(" ".join(list).replace(" ", ""))

for num in cephalopod: 
    if num == "": 
        sum += total
    elif "*" in num or "+" in num: 
        operation = num[-1]
        total = int(num[:-1])
    elif operation == "*": 
        total *= int(num)
    elif operation == "+": 
        total += int(num)
sum += total

print("Part 2: " + str(sum))