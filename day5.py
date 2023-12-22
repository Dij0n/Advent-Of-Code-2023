def organizeData(lines):
    maps = {}
    currentKey = ""
    for line in lines:
        if (line.replace(" ", '').isnumeric()):
            lineTuple = (line.split(" ")[0], line.split(" ")[1], line.split(" ")[2])
            maps[currentKey].append(lineTuple)
        elif (line == ''):
            continue
        else:
            currentKey = line.split(" ")[0]
            maps[currentKey] = []
    return(maps)

with open ("Inputs/day5.txt") as file: lines = file.readlines()

lines = [line.rstrip("\n") for line in lines]
seeds = lines[0][7:].split() #Array of seed numbers
maps = organizeData(lines[2:]) #Organizes mapping data into arrays of tuples

finalSeedArray = []

for num in seeds:
    seed = int(num)
    for key in maps:
        for map in maps[key]:
            mapBounds = range(int(map[1]), int(map[1]) + int(map[2]))
            if (seed in mapBounds):
                seed += int(map[0]) - int(map[1])
                break
    finalSeedArray.append(seed)
    print(seed)

