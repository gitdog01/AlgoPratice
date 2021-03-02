import sys
N = int(sys.stdin.readline().replace("\n", ""))
visited = [[False for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if visited[i][j] != True:
            print("")
