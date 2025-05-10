from functions import file_input, print_solution

data = file_input("AoC-20-1-1.txt")
target = 2020
Part2 = "In Progress"

i = 0
j = 1
nums = []

for i in range(i, len(data) - 1): 
    print("i = " + str(i))
    for j in range(j, len(data)): 
        print(str(data[i]) + " and " + str(data[j]))
        if data[i] + data[j] == target: 
            nums = [data[i], data[j]]
        j += 1
    i += 1
    j = 0

Part1 = nums[0] * nums[1]

print_solution(Part1, Part2)