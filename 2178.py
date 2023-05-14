import collections

N, M = input().split()
Q = int(N)
V = int(M)
visited = [[False for _ in range(V)] for _ in range(Q)]
maze = [[] for _ in range(Q)]
for i in range(Q):
    maze[i] = list(input())

direction = [[0, 1],  [1, 0], [0, -1], [-1, 0]]

queue = collections.deque([[0, 0, 1]])


def solve():
    while queue:
        ny, nx, nc = queue.popleft()
        for move in direction:
            dy, dx = move
            if Q > dy + ny > -1 and V > dx + nx > -1 and visited[dy + ny][dx + nx] == False and maze[dy + ny][dx + nx] == "1":
                visited[ny][nx] = True
                queue.append([dy+ny, dx+nx, nc+1])

                if dy+ny == Q-1 and dx+nx == V-1:
                    return print(nc + 1)


solve()
