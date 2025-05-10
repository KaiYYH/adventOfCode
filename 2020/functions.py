def file_input(file): # Read file and return array
    input = open(file, 'r')
    data = []

    for i in input: 
        data.append(int(i.strip("\n")))

    return data

def print_solution(Part1, Part2) : # Print solutions
    print("Part 1: " + str(Part1))
    print("Part 2: " + str(Part2))