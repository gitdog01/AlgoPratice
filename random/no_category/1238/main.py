import sys
import heapq
N, M, X = map(int, sys.stdin.readline().replace("\n", "").split())
load = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
total = [0 for _ in range(N+1)]

for _ in range(M):
    start, end, time = map(int, sys.stdin.readline().replace("\n", "").split())
    load[start][end] = time

for i in range(1, N+1):
    temp = [sys.maxsize for _ in range(N+1)]

    total[i]
