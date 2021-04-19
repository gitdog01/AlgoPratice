import sys


N, M = map(int, sys.stdin.readline().replace("\n", "").split())
Truth = list(map(int, sys.stdin.readline().replace("\n", "").split()))
connect = [[0 for _ in range(N+1)] for _ in range(N+1)]
partys = [[] for _ in range(M)]
visited = [False for _ in range(N+1)]
for i in range(M):
    p = list(map(int, sys.stdin.readline().replace("\n", "").split()))
    partys[i] = p[1:]
    for y in range(len(partys[i])):
        for x in range(y, len(partys[i])):
            connect[partys[i][y]][partys[i][x]] = 1
            connect[partys[i][x]][partys[i][y]] = 1
Truth = Truth[1:]
for one in Truth:
    visited[one] = True
    queue = [one]

    while queue:
        now = queue.pop()
        for c in range(len(connect[now])):
            if connect[now][c] == 1 and visited[c] == False:
                visited[c] = True
                queue.append(c)

answer = 0
for party in partys:
    fake = True
    for person in party:
        if visited[person]:
            fake = False
            break
    if fake:
        answer += 1
print(answer)
