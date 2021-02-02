# 01:02:41.91
import sys
moves = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
while True:
    x, y = map(int, sys.stdin.readline().split(' '))
    if x == 0 and y == 0:
        break
    island = []
    visited = [[False for _ in range(x)] for _ in range(y)]

    for _ in range(y):
        island.append(list(map(int, sys.stdin.readline().split(' '))))
    visited_num = sum([island[i].count(1) for i in range(y)])

    stack = []
    answer = 0
    while visited_num != 0:
        new = [0, 0]
        lx = 0
        ly = 0
        for ydx in range(ly, len(island)):
            for xdx in range(lx, len(island[0])):
                if (island[ydx][xdx] == 1) and (visited[ydx][xdx] != True):
                    new = [ydx, xdx]
                    break
        stack.append(new)
        visited[new[0]][new[1]] = True
        visited_num -= 1
        while stack:
            now = stack.pop()
            for move in moves:
                dy = now[0]+move[0]
                dx = now[1]+move[1]
                if not (len(island[0]) > dx >= 0 and len(island) > dy >= 0):
                    continue
                if (visited[dy][dx] != True) and (island[dy][dx] == 1):
                    stack.append([dy, dx])
                    visited[dy][dx] = True
                    visited_num -= 1
        answer += 1
    print(answer)
