import sys
import collections


def find(n, m, maze):
    visited = [[False for _ in range(m)] for _ in range(n)]
    b_visited = [[False for _ in range(m)] for _ in range(n)]
    queue = collections.deque([[0, 0, 1, False]])
    visited[0][0] = True
    b_visited[0][0] = True
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    while queue:
        ny, nx, count, break_wall = queue.popleft()
        if ny == n-1 and nx == m-1:
            return count
        for move in moves:
            dy, dx = move
            if n > ny + dy > -1 and m > nx + dx > -1:
                if break_wall == False and visited[ny+dy][nx+dx] == False:
                    visited[ny+dy][nx+dx] = True
                    if maze[ny+dy][nx+dx] == "0":
                        queue.append([ny+dy, nx+dx, count+1, False])
                    else:
                        queue.append([ny+dy, nx+dx, count+1, True])
                if break_wall == True and b_visited[ny+dy][nx+dx] == False and maze[ny+dy][nx+dx] == "0":
                    b_visited[ny+dy][nx+dx] = True
                    queue.append([ny+dy, nx+dx, count+1, break_wall])

    return -1


N, M = map(int, sys.stdin.readline().replace("\n", "").split())
maze = []
for _ in range(N):
    maze.append(list(sys.stdin.readline().replace("\n", "")))
print(find(N, M, maze))
