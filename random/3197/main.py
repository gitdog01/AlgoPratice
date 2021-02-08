import sys


def melt(l, y, x):
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for move in moves:
        dy, dx = move
        if not (len(l) > y+dy >= 0 and len(l[0]) > x+dx >= 0):
            continue
        if l[y+dy][x+dx] == '.' or l[y+dy][x+dx] == 'L':
            l[y][x] = '#'


def find(l, y, x, v):
    if l[y][x] == 'X' or v[y][x] == True:
        return False
    if l[y][x] == 'L':
        return True
    v[y][x] = True


R, C = map(int, sys.stdin.readline().replace("\n", "").split(" "))
lake = []
for _ in range(R):
    lake.append(list(sys.stdin.readline().replace("\n", "")))
day = 0

while day < 5:
    breaker = False
    for y in range(R):
        for x in range(C):
            if lake[y][x] == 'L':
                visited = [[False for _ in range(R)] for _ in range(C)]
                visited[y][x] = True
                if find(lake, y, x, visited):
                    print(day)
                    sys.exit()
                else:
                    breaker = True
                    break
            if breaker == True:
                break

    for y in range(R):
        for x in range(C):
            if lake[y][x] == 'X':
                melt(lake, y, x)

    for y in range(R):
        for x in range(C):
            if lake[y][x] == '#':
                lake[y][x] = '.'
    day += 1
