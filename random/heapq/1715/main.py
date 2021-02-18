import sys
import heapq

queue = []
N = int(sys.stdin.readline().replace("\n", ""))
for _ in range(N):
    heapq.heappush(queue, int(sys.stdin.readline().replace("\n", "")))
result = 0
last = 0
if len(queue) == 2:
    result = heapq.heappop(queue) + heapq.heappop(queue)
elif len(queue) == 1:
    result = heapq.heappop(queue)
else:
    while queue:
        now = heapq.heappop(queue)
        if last == 0:
            last = now + heapq.heappop(queue)
            result = last
        else:
            result += last + now

print(result)
