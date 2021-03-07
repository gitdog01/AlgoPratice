import sys
import heapq
N, M = map(int, sys.stdin.readline().replace("\n", "").split(" "))
maze = []
for _ in range(M):
    maze.append(list(sys.stdin.readline().replace("\n", "")))

dp = [[sys.maxsize for _ in range(N)] for _ in range(M)]
dp[0][0] = 0
answer = sys.maxsize

queue = []
heapq.heappush(queue, (0, [0, 0]))

moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]

while queue:
    w, now = heapq.heappop(queue)
    ny, nx = now
    if w > dp[ny][nx]:
        continue

    for dy, dx in moves:
        if M > ny+dy > -1 and N > nx+dx > -1 and w + int(maze[ny+dy][nx+dx]) < dp[ny+dy][nx+dx]:
            dp[ny+dy][nx+dx] = w + int(maze[ny+dy][nx+dx])
            heapq.heappush(queue, (w+int(maze[ny+dy][nx+dx]), [ny+dy, nx+dx]))
print(dp[M-1][N-1])
