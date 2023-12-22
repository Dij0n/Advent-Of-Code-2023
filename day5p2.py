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

def updateRanges(seedRange, map):
    finalSeedGroup = []
    for seedRange in seedGroup:
        mapUpperBound = int(map[1]) + int(map[2]) - 1 # Looots of definitions for readability,
        mapLowerBound = int(map[1])                   # without these it gets really messy
        difference = int(map[0]) - int(map[1])
        mapBounds = (mapLowerBound, mapUpperBound)
        intersect = (-1, -1) if (mapLowerBound > seedRange[1] or mapUpperBound < seedRange[0]) else (max(seedRange[0], mapLowerBound), min(seedRange[-1], mapUpperBound))

        print("        Curre | " + str(seedRange) + "\n        Bound | " + str(mapBounds) + "\n        Inter | " + str(intersect) + "\n        Diffr | " + str(difference))

        finalSeedGroup.append((seedRange[0], seedRange[1]))

        if (intersect == seedRange):
            #Both included, adding to both
            finalSeedGroup[-1] = (seedRange[0] + difference, seedRange[1] + difference)
            print("         Double Addition")
        elif (intersect[1] == seedRange[1]):
            #Second included, adding to second
            finalSeedGroup[-1] = (seedRange[0], intersect[0] - 1)
            finalSeedGroup.append((intersect[0] + difference, intersect[1] + difference))
            print("         Second Addition")
        elif (intersect[0] == seedRange[0]):
            #First included, adding to first
            finalSeedGroup[-1] = (intersect[0] + difference, intersect[1] + difference)
            finalSeedGroup.append((intersect[1] + 1, seedRange[1]))
            print("         First Addition")
        
    print("Result    | " + str(finalSeedGroup))
    return(finalSeedGroup)
    




with open ("Inputs/day5.txt") as file: lines = file.readlines()

lines = [line.rstrip("\n") for line in lines]
seeds = lines[0][7:].split() 
seedGroups = [[(int(seeds[i]), int(seeds[i]) + int(seeds[i+1]))] for i in range(0, len(seeds), 2)] #Array of seed number ranges (stored in tuples)
maps = organizeData(lines[2:]) #Organizes mapping data into arrays of tuples

print(seedGroups)

finalSeedGroups = []

for seedGroup in seedGroups:
    for key in maps:
        nextGroupIteration = []
        for map in maps[key]:


            print("SeedGroup | " + str(seedGroup))
            updatedRanges = updateRanges(seedGroup, map)

            toRemove = []
            for uRange in updatedRanges:
                if uRange not in seedGroup:
                    nextGroupIteration.append(uRange)
                    toRemove.append(uRange)
            
            for to in toRemove: updatedRanges.remove(to)

            seedGroup = updatedRanges
            print("\nSeedGroup | " + str(updatedRanges))
            if(not seedGroup):
                break
        seedGroup = nextGroupIteration + updatedRanges
        print("Final | " + str(seedGroup))
        print("NEXT KEY!!!!!!!!!!!!!!!!!!!!!!!!")

    finalSeedGroups.append(seedGroup)

finalSeedGroupsUnpacked = [num for group in finalSeedGroups for range in group for num in range]

print(min(finalSeedGroupsUnpacked))