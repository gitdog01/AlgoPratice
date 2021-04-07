import sys
sys.setrecursionlimit(1000000)


def find(ny, nx, dp, maze, visited):
    if ny == len(maze)-1 and nx == len(maze[0])-1:
        return 1
    if visited[ny][nx]:
        return dp[ny][nx]
    visited[ny][nx] = True
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for move in moves:
        dy, dx = move
        if len(maze) > ny+dy > -1 and len(maze[0]) > nx+dx > -1 and maze[ny][nx] > maze[ny+dy][nx+dx]:
            dp[ny][nx] += find(ny+dy, nx+dx, dp, maze, visited)

    return dp[ny][nx]


Y, X = map(int, sys.stdin.readline().replace("\n", "").split())
maze = []
dp = [[0 for _ in range(X)] for _ in range(Y)]
visited = [[False for _ in range(X)] for _ in range(Y)]
for _ in range(Y):
    maze.append(list(map(int, sys.stdin.readline().replace("\n", "").split())))

find(0, 0, dp, maze, visited)

print(dp[0][0])
