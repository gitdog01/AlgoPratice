# 문제가 이상함
import sys
import heapq
N, M, X = map(int, sys.stdin.readline().split())
town = {}
for _ in range(M):
    start, end, time = map(int, sys.stdin.readline().split())
    if start not in town:
        town[start] = []
    town[start].append((time, end))

answer = 0

queue = []
heapq.heappush(queue, (0, X))
back = [sys.maxsize for _ in range(N+1)]
back[X] = 0

while queue:
    time, now = heapq.heappop(queue)

    for next_time, next_town in town[now]:
        if back[next_town] < next_time + time:
            continue
        back[next_town] = next_time + time
        heapq.heappush(queue, (time+next_time, next_town))


for i in range(1, N+1):
    if i == X:
        continue
    queue = []
    heapq.heappush(queue, (0, i))

    visited = [sys.maxsize for _ in range(N+1)]
    visited[i] = 0

    while queue:
        time, now = heapq.heappop(queue)

        for next_time, next_town in town[now]:
            if visited[next_town] < next_time + time:
                continue
            visited[next_town] = next_time + time
            heapq.heappush(queue, (time+next_time, next_town))
    answer = max(answer, visited[X]+back[i])
print(answer)
