# read file
file_input = []
with open(r'C:\Users\kyray\OneDrive\Documents\Advent of Code 2023\Dec2Input.txt') as f:
        for line in f:
                file_input.append(line)

possible_games = []

for k in file_input: 
    # default possibility
    possible = True
    # removing \n from line
    file_input_stripped = k.rstrip('\n')

    # splitting for game number
    game_split = file_input_stripped.split(': ')
    game_number = game_split[0].split(' ')

    # splitting for sets
    set_split = game_split[1].split('; ')

    # determining if possible for each set
    for i in set_split: 
        # split to colours
        colours = []
        red = 0
        blue = 0
        green = 0

        colours = i.split(', ')

        # split number and colour
        for j in colours: 
            count = j.split(' ')

            # count each
            if count[1] == "red": 
                red = red + int(count[0])
            elif count[1] == "blue": 
                blue = blue + int(count[0])
            else: 
                green = green + int(count[0])

        # checking if possible
        if red > 12 or green > 13 or blue > 14: 
            possible = False
            break
        else: 
            continue

    # adding game number to array if the game is possible
    if possible == True: 
        possible_games.append(game_number[1])
    else: 
        continue

# sum of possible games array
sum = 0
for n in possible_games:
        sum = sum + int(n)
 
print(sum)