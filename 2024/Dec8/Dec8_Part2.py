input = open("Dec8_Input.txt", "r")

fmap = []
frequencies = {}
antinodes = []

for i in input: 
    fmap.append(list(i.replace("\n", "")))

for x in fmap: 
    for y in x: 
        if y != "." and y not in frequencies: 
            frequencies |= {y: []}

for frequency in frequencies.keys(): 
    locations = []
    for x in range(len(fmap)): 
        for y in range(len(fmap[x])): 
            if frequency == fmap[x][y]: 
                locations.append([x, y])
                antinodes.append([x, y])
                
    frequencies[frequency] = locations

for antennas in frequencies.values(): 
    for antenna in range(len(antennas) - 1): 
        for next_antenna in range(antenna + 1, len(antennas)): 

            difference = [antennas[next_antenna][0] - antennas[antenna][0], antennas[next_antenna][1] - antennas[antenna][1]]

            multiplier = 1

            while antennas[next_antenna][0] + multiplier*difference[0] in range(len(fmap)) and antennas[next_antenna][1] + multiplier*difference[1] in range(len(fmap)): 
                if [antennas[next_antenna][0] + multiplier*difference[0], antennas[next_antenna][1] + multiplier*difference[1]] not in antinodes: 
                    antinodes.append([antennas[next_antenna][0] + multiplier*difference[0], antennas[next_antenna][1] + multiplier*difference[1]])
                multiplier += 1
            
            multiplier = 1

            while antennas[antenna][0] - multiplier*difference[0] in range(len(fmap)) and antennas[antenna][1] - multiplier*difference[1] in range(len(fmap)): 
                if [antennas[antenna][0] - multiplier*difference[0], antennas[antenna][1] - multiplier*difference[1]] not in antinodes: 
                    antinodes.append([antennas[antenna][0] - multiplier*difference[0], antennas[antenna][1] - multiplier*difference[1]])
                multiplier += 1

print(len(antinodes))