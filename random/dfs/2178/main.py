import sys
import collections


def solve():
    Y, X = map(int, sys.stdin.readline().replace("\n", "").split(" "))
    maze = []
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    queue = collections.deque([[0, 0, 0]])
    visited = [[False for _ in range(X)] for _ in range(Y)]
    for _ in range(Y):
        maze.append(list(sys.stdin.readline().replace("\n", "")))
    while queue:
        ny, nx, count = queue.popleft()
        for move in moves:
            dy, dx = move
            if Y > ny+dy > -1 and X > nx+dx > -1 and maze[ny+dy][nx+dx] == "1" and visited[ny+dy][nx+dx] == False:
                visited[ny+dy][nx+dx] = True
                queue.append([ny+dy, nx+dx, count+1])
                if ny+dy == Y - 1 and nx+dx == X - 1:
                    return count+2


print(solve())
