import sys
import collections


def solve():
    X, Y, Z = map(int, sys.stdin.readline().replace("\n", "").split(" "))
    fresh = 0
    boxs = []
    queue = collections.deque([])
    for _ in range(Z):
        box = []
        for _ in range(Y):
            box.append(list(sys.stdin.readline().replace("\n", "").split(" ")))
        boxs.append(box)
    for z in range(Z):
        for y in range(Y):
            for x in range(X):
                if boxs[z][y][x] == "1":
                    queue.append([z, y, x, 0])
                elif boxs[z][y][x] == "0":
                    fresh += 1
    moves = [[0, 0, 1], [0, 1, 0], [0, 0, -1],
             [0, -1, 0], [1, 0, 0], [-1, 0, 0]]
    while queue:
        nz, ny, nx, day = queue.popleft()
        for move in moves:
            dz, dy, dx = move
            if Z > nz+dz > -1 and Y > ny+dy > -1 and X > nx+dx > -1 and boxs[nz+dz][ny+dy][nx+dx] == "0":
                fresh -= 1
                boxs[nz+dz][ny+dy][nx+dx] = "1"
                queue.append([nz+dz, ny+dy, nx+dx, day+1])
    if fresh == 0:
        return day
    else:
        return -1


print(solve())
