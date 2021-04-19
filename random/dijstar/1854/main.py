import sys
import heapq
n, m, k = map(int, sys.stdin.readline().replace("\n", "").split())
dij = [[sys.maxsize for _ in range(k)] for _ in range(n+1)]
town = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().replace("\n", "").split())
    town[a].append((c, b))

queue = []
heapq.heappush(queue, (0, 1))
dij[1][0] = 0
while queue:
    time, now = heapq.heappop(queue)

    for next_time, next_town in town[now]:

        if dij[next_town][k-1] > time+next_time:
            dij[next_town][k-1] = (time+next_time)
            dij[next_town] = sorted(dij[next_town])
            heapq.heappush(queue, (time+next_time, next_town))
for i in range(1, n+1):
    print(-1 if dij[i][k-1] == sys.maxsize else dij[i][k-1])
