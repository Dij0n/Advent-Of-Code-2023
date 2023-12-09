
def findDiffs(nums): #Returns array with differences between numbers
    diffs = []
    for i in range(len(nums) - 1):
        diffs.append(int(nums[i+1]) - int(nums[i]))
    return(diffs)

def findExtension(nums): #Recursive function to find next number in list
    if (len(set(nums)) == 1):
        return(nums[0])
    else:
        return(int(nums[0]) - findExtension(findDiffs(nums)))


with open ("Inputs/day9.txt") as file: lines = file.readlines()

final = []

for line in lines:
    line = line.rstrip('\n').split(" ")
    final.append(findExtension(line))

print(sum(final))


