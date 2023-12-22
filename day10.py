def crawlThroughPipes(pipe, dir, coords):

    pipeDict = {
        "|": ["U", "D"],
        "-": ["L", "R"],
        "L": ["D", "L"],
        "J": ["D", "R"],
        "7": ["U", "R"],
        "F": ["U", "L"]
    }   
    pipeDict[pipe].remove(dir)
    dirNext = pipeDict[pipe][0]

    match dirNext:
        case "U":
            dirNext = "D"
            coordsNext = (coords[0] + 1, coords[1] + 0)
        case "D":
            dirNext = "U"
            coordsNext = (coords[0] - 1, coords[1] + 0)
        case "L":
            dirNext = "R"
            coordsNext = (coords[0] + 0, coords[1] + 1)
        case "R":
            dirNext = "L"
            coordsNext = (coords[0] + 0, coords[1] - 1)

    pipeNext = grid[coordsNext[0]][coordsNext[1]]

    print(pipeNext + "     " + dirNext  + "     " + str(coordsNext))

    return(pipeNext, dirNext, coordsNext)

with open("Inputs/day10.txt") as file: grid = [list(line.rstrip('\n')) for line in file]

coords = [(i, line.index("S")) for i, line in enumerate(grid) if "S" in line][0]
direction = ""
pipe = ""

Up, Down, Left, Right = grid[coords[0] - 1][coords[1]], grid[coords[0] + 1][coords[1]], grid[coords[0]][coords[1] - 1], grid[coords[0]][coords[1] + 1]

if Up == "|" or Up == "7" or Up == "F":
    direction = "U"
    pipe = "|"
elif Down == "|" or Down == "L" or Down == "J":
    direction = "D"
    pipe = "|"
elif Left == "-" or Left == "L" or Left == "F":
    direction = "L"
    pipe = "-"
elif Right == "-" or Right == "7" or Right == "J":
    direction = "R"
    pipe = "-"

steps = 0
while pipe != "S":
    steps += 1
    pipe, direction, coords = crawlThroughPipes(pipe, direction, coords)

print(steps/2)