def expandGrid(grid):
    newGrid = [list("".join(row).replace(".", "M")) if "#" not in row else row for row in grid]

    for i in range(len(newGrid[0])):
        colList = [row[i] for row in newGrid]
        if "#" not in colList:
            for row in newGrid: row[i] = "M"
    
    return(newGrid)
        
with open("Inputs/day11.txt") as file: grid = [list(line.rstrip('\n')) for line in file]

grid = expandGrid(grid)

for i in grid: print(i)

stars = []
relativeCoords = [0, 0]
stepSize = 999999

for row in grid:
    if "." not in row: 
        relativeCoords[0] += stepSize + 1
        continue
    for point in row:
        if point == "M": relativeCoords[1] += stepSize
        if point == "#": stars.append((relativeCoords[0], relativeCoords[1]))
        relativeCoords[1] += 1
    relativeCoords[0] += 1
    relativeCoords[1] = 0
    
print(stars)

starPairs = [(stars[x], stars[y]) for x in range(len(stars)) for y in range(x + 1, len(stars))]
starDists = [abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]) for pair in starPairs]
#starDists = [abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]) for pair in [([(i, j) for i, row in enumerate(grid) for j, point in enumerate(row) if point == "#"][x], [(i, j) for i, row in enumerate(grid) for j, point in enumerate(row) if point == "#"][y]) for x in range(len([(i, j) for i, row in enumerate(grid) for j, point in enumerate(row) if point == "#"])) for y in range(x + 1, len([(i, j) for i, row in enumerate(grid) for j, point in enumerate(row) if point == "#"]))]]

print(sum(starDists))

