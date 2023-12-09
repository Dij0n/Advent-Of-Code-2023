wordDict = {'one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9',}

def wordsToNums(line):
    scanningLine = ''

    for letter in line:
        scanningLine += letter

        for key in wordDict:
            scanningLine = scanningLine.replace(key, wordDict[key])

    return(scanningLine)

total = 0

with open("Inputs\day1.txt") as file:
    for line in file:
        convertedLine = wordsToNums(line)
        noAlpha = [num for num in convertedLine if num.isnumeric()]
        total += int(noAlpha[0] + noAlpha[-1])

print(total)

sol = sum([1 if i%3==0 or i%4==0 else 0 for i in range(100,1000)])
print(sol)


    

