from functions import file_input, print_solution

data = file_input("AoC-20-1.txt")
target = 2020

# PART 1
i = 0
j = 1
nums = []

for i in range(i, len(data) - 1): 
    for j in range(j, len(data)): 
        if int(data[i]) + int(data[j]) == target: 
            nums = [data[i], data[j]]
        j += 1
    i += 1
    j = i + 1

Part1 = int(nums[0]) * int(nums[1])

# PART 2
i = 0
j = 1
k = 2
nums = []

for i in range(i, len(data) - 2): 
    for j in range(j, len(data) - 1): 
        for k in range(k, len(data)): 
            if int(data[i]) + int(data[j]) + int(data[k]) == target: 
                nums = [data[i], data[j], data[k]]
            k += 1
        j += 1
        k = j + 1
    i += 1
    j = i + 1
    k = j + 1

Part2 = int(nums[0]) * int(nums[1]) * int(nums[2])

print_solution(Part1, Part2)