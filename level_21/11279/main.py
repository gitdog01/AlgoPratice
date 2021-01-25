import heapq
import sys
N = int(input())
myHeap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(myHeap) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(myHeap))
    else:
        heapq.heappush(myHeap, (-num))
