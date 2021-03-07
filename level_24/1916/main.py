# 첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다.
import sys
import heapq
N = int(sys.stdin.readline().replace("\n", ""))
M = int(sys.stdin.readline().replace("\n", ""))
graph = [[]for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().replace("\n", "").split(" "))
    graph[a].append((c, b))
S, E = map(int, sys.stdin.readline().replace("\n", "").split(" "))
queue = []
dp = [sys.maxsize for _ in range(N+1)]
dp[S] = 0
heapq.heappush(queue, (0, S))
while queue:
    # print("queue :", queue)
    w, now = heapq.heappop(queue)
    if dp[now] < w:
        continue
    # print("now  : ", now, "/ weigt : ", w)
    for value, next_key in graph[now]:
        # print(value, next_key)
        if value + w < dp[next_key]:
            dp[next_key] = value+w
            # print("dp   : ", dp)
            heapq.heappush(queue, (value+w, next_key))
    # print("=====================")
print(dp[E])
# print(dp)
