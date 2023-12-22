def isValid(springs, data):
    counts = [len(s) for s in list(filter(None, springs.split(".")))]
    return counts == [int(x) for x in data]

def allPossible(springs):
    qPositions = [pos for pos, i in enumerate(springs) if i == "?"]
    count = bin(pow(2, len(qPositions)))
    totalCombos = []


    while len(count[3:]) <= len(qPositions):
        tempArray = list(springs)
        for bi, pos in enumerate(qPositions):
            if int(count[-(bi + 1)]): 
                tempArray[pos] = "#" 
            else: 
                tempArray[pos] = "."

        totalCombos.append("".join(tempArray))
        count = bin(int(count, 2) + 1)

    return(totalCombos)

with open ("Inputs/day12.txt") as file: lines = file.readlines()
springDict = [(line[0], line[1].rstrip('\n').split(",")) for line in [line.split(" ") for line in lines]]

count = 0
lines = 0
for key in springDict:
    print(lines, count, key[0])
    for line in allPossible(key[0]):
        if isValid(line, key[1]): count += 1    
    lines += 1

print(count)