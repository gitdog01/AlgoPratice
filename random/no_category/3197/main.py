import sys
sys.setrecursionlimit(1000000)


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
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for move in moves:
        dy, dx = move
        if not (len(l) > y+dy >= 0 and len(l[0]) > x+dx >= 0) and l[y+dy][x+dx] != 'X' and v[y+dy][x+dx] != True:
            continue
        if find(l, y+dy, x+dx, v):
            return True
    return False


R, C = map(int, sys.stdin.readline().replace("\n", "").split(" "))
lake = []
for _ in range(R):
    lake.append(list(sys.stdin.readline().replace("\n", "")))
day = 0
onetime = False
for y in range(R):
    for x in range(C):
        if lake[y][x] == 'L':
            lake[y][x] = 'S'
            onetime = True
            break
    if onetime:
        break

while day < 5:
    breaker = False
    for y in range(R):
        for x in range(C):
            if lake[y][x] == 'S':
                visited = [[False for _ in range(C)] for _ in range(R)]
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
