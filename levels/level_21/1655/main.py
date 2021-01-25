import heapq
import sys

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    heap.append(num)
    heapq.heapify(heap)
    print(heap)
