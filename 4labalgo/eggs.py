xy = []
result = []


def algo(iterator):

    def length89(x1, y1, x2, y2):
        length = pow(pow(x2 - x1, 2) + pow(y2 - y1, 2), 0.5)
        return length

    coordinats = []
    lengths = []
    for firstC in xy:
        for secondC in xy:
            lengths.append(length89(firstC[0], firstC[1], secondC[0], secondC[1]))
            coordinats.append([firstC, secondC, length89(firstC[0], firstC[1], secondC[0], secondC[1])])
    n = 2

    def sort_col(i):
        return i[n]

    coordinats.sort(key=sort_col)

    maxlengthC = coordinats[0 - iterator]

    drawLineCoordinats = []

    def draw_line(x1=0.00, y1=0.00, x2=0.00, y2=0.00):
        x1 = x1 * 10.00
        y1 = y1 * 10.00
        x2 = x2 * 10.00
        y2 = y2 * 10.00
        deltaX = (x2 - x1)
        deltaY = (y2 - y1)
        signX = 1.00 if x1 < x2 else -1.00
        signY = 1.00 if y1 < y2 else -1.00
        error = deltaX - deltaY
        while (x1 != x2 or y1 != y2):
            error2 = error * 2
            if error2 > -deltaY:
                error = error - deltaY
                x1 = x1 + signX
            if error2 < deltaX:
                error = error + deltaX
                y1 = y1 + signY
            drawLineCoordinats.append([y1 / 10.00, x1 / 10.00])
        del drawLineCoordinats[-1]

    draw_line((maxlengthC[1][1]), (maxlengthC[1][0]), (maxlengthC[0][1]), (maxlengthC[0][0]))

    result.append(maxlengthC[2])
    searchElements(drawLineCoordinats, xy, iterator)


def searchElements(drawLineCoordinats, xy, iterator):
    for i in drawLineCoordinats:
        if i in xy:
            iterator = iterator + 2
            algo(iterator)


if __name__ == '__main__':
    x = [2, 0, 1, 2]
    y = [0, 0, 5, 10]

    for i in range(len(x)):
        xy.append([x[i], y[i]])

    iterator = 1
    algo(iterator)
    print(result[-1])




