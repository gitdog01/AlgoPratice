import sys
import collections
Y, X = map(int, sys.stdin.readline().replace("\n", "").split(" "))
origin = []
for _ in range(Y):
    origin.append(list(sys.stdin.readline().replace("\n", "")))


def bfs(y, x):
    moves = [[0, 1], [1, 0], [1, 1]]
    visited = [[False for _ in range(X)] for _ in range(Y)]
    count = 0
    head = origin[y][x]

    queue = collections.deque([y, x])

    while queue:
        ny, nx = queue.popleft()
        for move in moves:
            dy, dx = move
