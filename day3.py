grid = []
gearDict = {}

def grabAround(i, j):
    return [(x, y) for y in range(j-1, j+2) for x in range(i-1, i+2)]

def symbolAround(i, j, nextNum):
    numCoords = [(x, j) for x in range (i - len(nextNum), i)]
    for x, y in numCoords:
        for xAr, yAr in grabAround(x, y):
            try:
                if (not grid[yAr][xAr].isnumeric() and grid[yAr][xAr] != '.' and yAr >= 0 and xAr >= 0 and grid[yAr][xAr] != '\n' and grid[yAr][xAr] == '*'):
                    if (xAr, yAr) in gearDict:
                        gearDict[(xAr, yAr)].append(int(nextNum))
                    else:
                        gearDict[(xAr, yAr)] = [int(nextNum)]
                    return
                    
            except:
                continue

with open ("Inputs/day3.txt") as file:
    grid = [[*line] for line in file]

    for row in grid: 
        print(row)

    nextNum = ''
    for j, row in enumerate(grid): #i is Hori, j is Verti
        for i, char in enumerate(row):
            if (char.isnumeric()):
                nextNum += char
            elif (nextNum != ''):
                symbolAround(i, j, nextNum)
                print(gearDict)
                nextNum = ''

    total = 0
    for coord in gearDict:
        if (len(gearDict[coord]) == 2):
            total += gearDict[coord][0] * gearDict[coord][1]
    
    print(total)