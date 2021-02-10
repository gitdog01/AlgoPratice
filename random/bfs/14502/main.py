import sys
import copy
import itertools
sys.setrecursionlimit(100000)


def virusSpread(l, y, x):
    moves = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    l[y][x] = 2
    for move in moves:
        dy, dx = move
        if (len(l) > y+dy >= 0) and (len(l[0]) > x+dx >= 0) and l[y+dy][x+dx] == 0:
            virusSpread(l, y+dy, x+dx)


Y, X = map(int, sys.stdin.readline().replace("\n", "").split(" "))
lab = []
zeros = []
virus = []
answer = 0
find = []
for _ in range(Y):
    lab.append(list(map(int, sys.stdin.readline().replace("\n", "").split(" "))))


for y in range(Y):
    for x in range(X):
        if lab[y][x] == 0:
            zeros.append([y, x])
        elif lab[y][x] == 2:
            virus.append([y, x])

candis = itertools.combinations(zeros, 3)
for candi in candis:
    tempCount = 0
    tempLab = copy.deepcopy(lab)
    for a in candi:
        ty, tx = a
        tempLab[ty][tx] = 1
    for b in virus:
        vy, vx = b
        virusSpread(tempLab, vy, vx)

    for line in tempLab:
        # print(line)
        tempCount += line.count(0)
    # print("="*X)
    answer = max(tempCount, answer)
print(answer)
