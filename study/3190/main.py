import sys
N = int(sys.stdin.readline().replace("\n", ""))
K = int(sys.stdin.readline().replace("\n", ""))
baaam = 1
time = 0
nx = 0
ny = 0

dx = 0
dy = 0

move = [[1, 0], [0, 1], [-1, 0], [-1, 0]]
point = 1

maze = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    x, y = map(int, sys.stdin.readline().replace("\n", "").split(" "))
    maze[y-1][x-1] = 3

L = int(sys.stdin.readline().replace("\n", ""))
events = []
for _ in range(L):
    events.append(sys.stdin.readline().replace("\n", "").split(" "))

tail = [0, 0]
while N > nx + dx > -1 and N > ny + dy > - 1 and maze[ny+dy][nx+dx] == 0:
    nx = nx+dx
    ny = ny+dy

    if maze[ny][nx] == 3:
        maze[ny][nx] = 1
    else:
        maze[ny][nx] = 1

    time += 1


print(time)
