#

num = 3
numX = 4

total = int((1 + num) * num / 2)

seedList = [i for i in range(numX)]

output = [i + 1 for i in range(numX)]

for index in range(len(output), 2, -1):
    nextBool = True
    while nextBool:
        for i in range(output[index-2], total):
            output[index-1] = i + 1
            print(index-1)
            print(output)
        output[index - 2] += 1
        output[index - 1] = output[index - 2] + 1
        if output[index - 2] == total:
            nextBool = False



