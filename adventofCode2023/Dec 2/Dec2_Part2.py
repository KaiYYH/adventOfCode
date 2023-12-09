# read file
file_input = []
with open(r'C:\Users\kyray\OneDrive\Documents\Advent of Code 2023\Dec2Input.txt') as f:
        for line in f:
                file_input.append(line)

cube_of_required = []

for k in file_input: 
    # removing \n from line
    file_input_stripped = k.rstrip('\n')

    # splitting for game number
    game_split = file_input_stripped.split(': ')
    game_number = game_split[0].split(' ')

    # splitting for sets
    set_split = game_split[1].split('; ')
    red = 0
    blue = 0
    green = 0
    
    # determining max values for each set
    for i in set_split: 
        # split to colours
        colours = []
        colours = i.split(', ')

        # split number and colour
        for j in colours: 
            count = j.split(' ')

            # replace max value if higher
            if count[1] == "red" and int(count[0]) > red: 
                red = int(count[0])
            elif count[1] == "blue" and int(count[0]) > blue: 
                blue = int(count[0])
            elif count[1] == "green" and int(count[0]) > green: 
                green = int(count[0])
    
    # add cube of max values to array
    cube_of_required.append(red*blue*green)

# sum of cube values array
sum = 0
for n in cube_of_required:
        sum = sum + int(n)
 
print(sum)