from math import sin, cos, pi


def vrashau(mas, ugol):
    p = [[0, 0], [0, 0],  [0, 0],  [0, 0]]  # new_square
    coor_cent = [(mas[0][0] + mas[2][0]) / 2, (mas[0][1] + mas[2][1]) / 2]
    for i in range(4):
        p[i][0] = (mas[i][0]-coor_cent[0])*cos(ugol)
        - (mas[i][1]-coor_cent[1])*sin(ugol)
        p[i][1] = (mas[i][0]-coor_cent[0])*sin(ugol)
        + (mas[i][1]-coor_cent[1])*cos(ugol)
        p[i][0] = p[i][0]+coor_cent[0]
        p[i][1] = p[i][1]+coor_cent[1]
        p[i] = tuple(p[i])
    print(p)


def mogy_kupit(towar, money):
    mogy_tovar = []
    for i in towar:
        if towar[i] <= money:
            mogy_tovar.append(i)
    print(mogy_tovar)


def destroy_something_extra_in_your_life(massive):
    new = set(massive)
    print(list(new))


def difference(massive1, massive2):
    new = []
    for i in massive1:
        for j in massive2:
            if i != j:
                new.append(i)
    print(list(set(new)))
vrashau(((0, 1), (1, 0), (0, -1), (-1, 0)), 0.8)
mogy_kupit({'kisilev': 80000, 'fopf': 0}, 100)
destroy_something_extra_in_your_life
(['physics', 'sleeping', 'sleeping', 'sleeping', 'sleeping'])
difference(['pen', 'pineapple'], ['apple', 'pen'])
