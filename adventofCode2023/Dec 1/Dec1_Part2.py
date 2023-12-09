# PART TWO
spelled_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
number_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
whole_number = []

# read file
file_input = []
with open(r'C:\Users\kyray\OneDrive\Documents\Advent of Code 2023\Dec1Input.txt') as f:
        for line in f:
                file_input.append(line)

# finding
for f in file_input: 
        # first occurrence

        first_instances = []

        for i in spelled_numbers:
                check = f.find(i)
                if check != -1: 
                        first_instances.append(f.find(i))

        occurrence = min(first_instances)

        for i in spelled_numbers: 
                if f.startswith(i, occurrence) == True: 
                        first_digit = i
                        break

        # print(first_digit)

        x = 0
        for i in spelled_numbers: 
                if first_digit == i: 
                        first_digit = number_values[x]
                        break
                x = x + 1

        # print(first_digit)

        # last occurrence

        last_instances = []
        
        for i in spelled_numbers:
                check = f.rfind(i)
                if check != -1: 
                        last_instances.append(f.rfind(i))

        occurrence = max(last_instances)

        for i in spelled_numbers: 
                if f.startswith(i, occurrence) == True: 
                        last_digit = i
                        break

        y = 0
        for i in spelled_numbers: 
                if last_digit == i: 
                        last_digit = number_values[y]
                        break
                y = y + 1

        # print(last_digit)
        
        # appending 
        whole_number.append(int(first_digit+last_digit))

# print(whole_number)

# sum
sum = 0
for n in whole_number:
        sum = sum + n
 
print(sum)