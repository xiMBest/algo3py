def inFile():
    worlds = []
    for strochka in open("wchain.in"):
        poloska = strochka.strip("\n")
        worlds.append(poloska)
    worlds.pop(0)
    worlds.sort(key=lambda w: len(w))
    return worlds


def amountSearch(firstLine, secondLine):
    firstCounter = 0
    secondCounter = 0
    amount = 0
    while firstCounter < len(firstLine) and secondCounter < len(secondLine):
        if firstLine[firstCounter] != secondLine[secondCounter]:
            amount += 1
            secondCounter -= 1
        firstCounter += 1
        secondCounter += 1
    return amount


if __name__ == "__main__":
    usedWorlds = inFile()
    outWorlds = [usedWorlds.pop(0)]

    for word in usedWorlds:
        lastAmount = 0
        lastAdded = outWorlds[-1]
        if len(word) - len(lastAdded) == 1:
            lastAmount = amountSearch(word, lastAdded)
            if lastAmount <= 1:
                outWorlds.append(word)
        elif len(word) == len(lastAdded):
            lastAmount = amountSearch(word, outWorlds[-2])
            if lastAmount <= 1:
                outWorlds.pop()
                outWorlds.append(word)
    print("-----------------------------------------")
    print("| Finish check your wchain.out file!!!  |")
    print("-----------------------------------------")
    outFile = open("wchain.out", 'w')
    outFile.write(str(len(outWorlds)))