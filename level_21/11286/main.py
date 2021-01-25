import heapq
import sys

N = int(sys.stdin.readline())
myHeap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(myHeap) == 0:
            print(0)
        else:
            print(heapq.heappop(myHeap)[1])
    else:
        heapq.heappush(myHeap, (abs(num), num))
