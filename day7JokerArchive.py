cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
handStorage = {"High":[],"One":[],"Two":[],"Three":[],"Full":[],"Four":[],"Five":[]}
with open("Inputs/day7.txt") as file: pairs = dict([line.rstrip('\n').split(" ") for line in file])

def findBestHand(hand):
    possibleHands = ['High']
    
    for card in hand:
        if card != 'J':
            match hand.count(card):
                case 5:
                    possibleHands.append('Five')
                    break
                case 4:
                    possibleHands.append('Four')
                    break
                case 3:
                    possibleHands.append('Three')
                case 2:
                    possibleHands.append('One')

                
    if 'One' in possibleHands: possibleHands.remove('One')
    if possibleHands.count('One') == 3:
        possibleHands = list(filter(('One').__ne__, possibleHands))
        possibleHands.append('Two')

    if 'Three' in possibleHands and 'One' in possibleHands:
        possibleHands.append('Full')
        
    possibleHands.sort(key = lambda i: list(handStorage).index(i), reverse=True)

    return possibleHands[0]

def imTheJokerFromTheBatman(handType):
    match handType:
        case 'High':
            return("One")
        case 'One':
            return("Three")
        case 'Two':
            return("Four")
        case 'Three':
            return("Four")
        case 'Four':
            return("Five")
        case 'Full':
            return("Four")
        case 'Five':
            return("Five")

for hand in pairs:

    bestHand = findBestHand(hand)

    for i in range(hand.count("J")):
        bestHand = imTheJokerFromTheBatman(bestHand)

    handStorage[bestHand].append(hand)


total = 0
multiplier = 1
for key in handStorage:
    handStorage[key].sort(key=lambda i: [cards.index(c) for c in i], reverse=True)
    for hand in handStorage[key]:
        print(key + "  " + str(multiplier) + "  " + hand + "  " + str(total))
        total += int(pairs[hand]) * multiplier
        multiplier += 1

print(total)