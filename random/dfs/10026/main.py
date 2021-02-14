import sys
sys.setrecursionlimit(100000)


def find(draw, y, x, visited, color):
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    visited[y][x] = True
    size_y = len(draw)
    size_x = len(draw[0])
    for move in moves:
        dy, dx = move
        if (size_y > y+dy >= 0) and (size_x > x+dx >= 0) and (visited[y+dy][x+dx] == False) and (draw[y+dy][x+dx] == color):
            find(draw, y+dy, x+dx, visited, color)


def find2(draw, y, x, visited, color):
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    visited[y][x] = True
    size_y = len(draw)
    size_x = len(draw[0])
    for move in moves:
        dy, dx = move
        if (size_y > y+dy >= 0) and (size_x > x+dx >= 0) and (visited[y+dy][x+dx] == False):
            if color == 'B' and draw[y+dy][x+dx] == 'B':
                find2(draw, y+dy, x+dx, visited, color)
            elif color != 'B' and draw[y+dy][x+dx] != 'B':
                find2(draw, y+dy, x+dx, visited, color)


N = int(sys.stdin.readline().replace("\n", ""))
visited = [[False for _ in range(N)]for _ in range(N)]
draw = []
for _ in range(N):
    draw.append(list(sys.stdin.readline().replace("\n", "")))

nomal_count = 0
for y in range(N):
    for x in range(N):
        if visited[y][x] == False:
            nomal_count += 1
            find(draw, y, x, visited, draw[y][x])

visited = [[False for _ in range(N)]for _ in range(N)]

redgreen_count = 0
for y in range(N):
    for x in range(N):
        if visited[y][x] == False:
            redgreen_count += 1
            find2(draw, y, x, visited, draw[y][x])

print(nomal_count, redgreen_count)
