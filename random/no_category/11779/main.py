import sys
import heapq
import collections
N = int(sys.stdin.readline().replace("\n", ""))
M = int(sys.stdin.readline().replace("\n", ""))

ways = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().replace("\n", "").split())
    ways[a].append((c, b))
start, end = map(int, sys.stdin.readline().replace("\n", "").split())

queue = []
heapq.heappush(queue, (0, start))
visited = [sys.maxsize for _ in range(N+1)]
visited[start] = 0
path = [-1 for _ in range(N+1)]


while queue:
    cost, now = heapq.heappop(queue)

    if visited[now] < cost:
        continue

    for next_location in ways[now]:
        next_cost, next_stop = next_location
        if visited[next_stop] > cost+next_cost:
            visited[next_stop] = cost+next_cost
            path[next_stop] = now
            heapq.heappush(queue, (cost+next_cost, next_stop))

trace = end
answers = collections.deque([])
while trace != -1:
    answers.appendleft(trace)
    trace = path[trace]

print(visited[end])
print(len(answers))
print(*answers)
