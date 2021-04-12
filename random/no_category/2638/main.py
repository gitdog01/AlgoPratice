import sys
sys.setrecursionlimit(10 ** 8)


def spread(y, x, cheeze, no_traps, visited):
    n = len(cheeze)
    m = len(cheeze[0])
    visited[y][x] = True
    no_traps.append([y, x])
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for move in moves:
        dy, dx = move
        if n > y + dy > -1 and m > x + dx > -1 and visited[y+dy][x+dx] == False and cheeze[y+dy][x+dx] == "0":
            visited[y+dy][x+dx] = True
            spread(y+dy, x+dx, cheeze, no_traps, visited)


N, M = map(int, sys.stdin.readline().replace("\n", "").split())
cheeze = []
remain = 0
time = 0
for _ in range(N):
    now = list(sys.stdin.readline().replace("\n", "").split())
    cheeze.append(now)
    remain += now.count("1")

while remain:
    time += 1
    disapear = []
    no_traps = []
    visited = [[False for _ in range(M)] for _ in range(N)]
    # 갇힌 애들 검사
    for y in range(0, N, N-1):
        for x in range(0, M, M-1):
            if cheeze[y][x] == "0" and visited[y][x] == False:
                spread(y, x, cheeze, no_traps, visited)

    for y in range(N):
        for x in range(M):
            if cheeze[y][x] == "1":
                count = 4
                moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for move in moves:
                    dy, dx = move
                    if N > y+dy > -1 and M > x+dx > -1 and cheeze[y+dy][x+dx] == "1":
                        count -= 1
                    elif N > y+dy > -1 and M > x+dx > -1 and cheeze[y+dy][x+dx] == "0" and [y+dy, x+dx] not in no_traps:
                        count -= 1
                if count >= 2:
                    disapear.append([y, x])
    for pang in disapear:
        py, px = pang
        cheeze[py][px] = "0"
        remain -= 1
print(time)
