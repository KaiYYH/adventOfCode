input = open("Dec6.txt", "r")
worksheet, totals, Part1 = [], [], 0

for i in input: 
    worksheet.append([item for item in i.replace("\n", "").strip().split(" ") if item.strip()])

for index in range(len(worksheet[0])): 
    if(worksheet[len(worksheet) - 1][index]) == "+": 
        total = 0
        for row_num in range(len(worksheet) - 1): 
            total += int(worksheet[row_num][index])
    elif(worksheet[len(worksheet) - 1][index]) == "*": 
        total = 1
        for row_num in range(len(worksheet) - 1): 
            total *= int(worksheet[row_num][index])
    totals.append(total)

for num in totals: Part1 += num

print("Part 1: " + str(Part1))