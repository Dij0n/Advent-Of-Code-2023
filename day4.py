import math

cards = {}

for i in range(250):
    cards[i] = 0

with open ("Inputs/day4.txt") as file:

    for cardNum, line in enumerate(file):
        winners = line[line.find(':') + 2 : line.find('|') - 1].rstrip('\n').split(" ")
        numbers = line[line.find('|') + 2:].rstrip('\n').split(" ")
        inArray = [1 for num in numbers if num in winners and num != '' ]
        score = sum(inArray)

        cards[cardNum] += 1

        for i in range(1, score + 1):
            cards[cardNum + i] += cards[cardNum]

    print(sum(cards.values()))


