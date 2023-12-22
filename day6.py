import math

with open ("Inputs/day6.txt") as file:
    lines = file.readlines()
    pairs = list(zip(lines[0][12:].rstrip('\n').split("     "), lines[1][12:].rstrip('\n').split("   ")))
    print(pairs)

    total = 1
    for pair in pairs:
        a = int(pair[0])
        x = int(pair[1])
        
        timeToHold = (-math.sqrt(-x + (pow(a, 2))/4) + a/2, math.sqrt(-x + (pow(a, 2))/4) + a/2)
        timeToHold = (math.ceil(timeToHold[0] + 0.001), math.floor(timeToHold[1] - 0.001))
        
        total *= (timeToHold[1] - timeToHold[0] + 1)
        print(total)
        