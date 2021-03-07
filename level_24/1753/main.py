import sys
import heapq
V, E = map(int, sys.stdin.readline().replace("\n", "").split(" "))
K = int(sys.stdin.readline().replace("\n", ""))
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().replace("\n", "").split(" "))
    graph[u].append((w, v))
dp = {}
dp[K] = 0

queue = []
heapq.heappush(queue, (0, K))
while queue:
    wei, now = heapq.heappop(queue)
    if now not in dp:
        dp[now] = sys.maxsize
    if dp[now] < wei:
        continue

    for w, next in graph[now]:
        if next not in dp:
            dp[next] = sys.maxsize
        if wei + w < dp[next]:
            dp[next] = wei + w
            heapq.heappush(queue, (wei + w, next))

for i in range(1, V+1):
    if i not in dp:
        print("INF")
    else:
        print(dp[i])
