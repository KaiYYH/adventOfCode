# PART ONE
import re

# read file
file_input = []
with open(r'C:\Users\kyray\OneDrive\Documents\Advent of Code 2023\Dec1Input.txt') as f:
        for line in f:
                file_input.append(line)

# finding 
whole_number = []
for x in file_input: 
        first = re.search(r'\d', x)
        final = re.findall(r'\d', x)[-1]
        if first and final:  
               whole_number.append(int(first.group()+final))

# sum
sum = 0
for x in whole_number:
        sum = sum + x
 
print(sum)