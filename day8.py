import math
with open ("Inputs/day8.txt") as file: lines = file.readlines()

instructions = lines[0].rstrip('\n')
instructions = instructions.replace("R", "1")
instructions = instructions.replace("L", "0")

mapDict = dict([(line[0:3], (line[7:10], line[12:15])) for line in lines[2:]])


mapsWithA = [key for key in mapDict if key[2] == "A"]
loopSteps = []

for direction in mapsWithA:
    currentDirection = direction
    steps = 0
    while currentDirection[2] != "Z":
        for i in instructions:
            currentDirection = mapDict[currentDirection][int(i)]
            steps += 1
            if (currentDirection[2] == "Z"): 
                loopSteps.append(steps)
                steps = 0
                break

print(loopSteps)