

def convertToNumbers(rawGame):
    colorArray = {'red': 0, 'green': 0, 'blue': 0}
    finalArray = []
    
    for pull in rawGame:
        pullArray = []
        for color in colorArray:

            if (color in pull): 
                if (pull[pull.find(color) - 3] == ' '):
                    numOfColor = int(pull[pull.find(color) - 2])
                else:
                    numOfColor = int(pull[pull.find(color) - 3 : pull.find(color) - 1])
            else:
                numOfColor = 0
            
            pullArray.append(numOfColor)
            if (numOfColor > colorArray[color]): colorArray[color] = numOfColor


        finalArray.append(pullArray)
    
    power = colorArray['red'] * colorArray['green'] * colorArray['blue']
    return(finalArray, power)
        


with open ("Inputs/day2.txt") as file:
    total = 0
    totalPart2 = 0
    for gameNum, game in enumerate(file):
        gameValid = True
        rawGame = game[game.find(':') + 1:].split(';')
        numGame, power = convertToNumbers(rawGame)

        for pull in numGame:
            for cubeNum, cube in enumerate(pull):
                if (cube - cubeNum > 12):
                    gameValid = False

        if (gameValid):
            total += gameNum + 1

        totalPart2 += power

        print(str(gameNum + 1) + " " + str(numGame) + " " + str(power))
    print(totalPart2)