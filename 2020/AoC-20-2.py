import re
from functions import file_input, print_solution

data = file_input("AoC-20-2.txt")
Part1 = 0
Part2 = 0

for line in data: 
    result = re.split(r"[-: ]", line)

    if result[4].count(result[2]) >= int(result[0]) and result[4].count(result[2]) <= int(result[1]): 
        Part1 += 1

    if (result[4][int(result[0]) - 1] == result[2] and result[4][int(result[1]) - 1] != result[2]) or (result[4][int(result[0]) - 1] != result[2] and result[4][int(result[1]) - 1] == result[2]): 
        Part2 += 1

print_solution(Part1, Part2)