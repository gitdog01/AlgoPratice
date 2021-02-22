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
    result = 0
else:
    while len(queue) > 1:
        now = heapq.heappop(queue)
        now2 = heapq.heappop(queue)
        result += now+now2
        heapq.heappush(queue, now+now2)

print(result)
# 다시 풀기
