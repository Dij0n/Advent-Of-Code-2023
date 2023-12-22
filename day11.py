def expandGrid(grid):
    newGrid = []

    for i, line in enumerate(grid):
        newGrid.append(list(line))
        if ("#" not in line): newGrid.append(line)

    for i in range(len(grid[0]) - 1, -1, -1):
        colChars = len(set([row[i] for row in grid]))
        if colChars == 1: 
            for newRow in newGrid: newRow.insert(i, ".")
    
    return(newGrid)
        
with open("Inputs/day11.txt") as file: grid = [list(line.rstrip('\n')) for line in file]

grid = expandGrid(grid)

stars = [(i, j) for i, row in enumerate(grid) for j, point in enumerate(row) if point == "#"]
starPairs = [(stars[x], stars[y]) for x in range(len(stars)) for y in range(x + 1, len(stars))]
starDists = [abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]) for pair in starPairs]
#starDists = [abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]) for pair in [([(i, j) for i, row in enumerate(grid) for j, point in enumerate(row) if point == "#"][x], [(i, j) for i, row in enumerate(grid) for j, point in enumerate(row) if point == "#"][y]) for x in range(len([(i, j) for i, row in enumerate(grid) for j, point in enumerate(row) if point == "#"])) for y in range(x + 1, len([(i, j) for i, row in enumerate(grid) for j, point in enumerate(row) if point == "#"]))]]

print(sum(starDists))

