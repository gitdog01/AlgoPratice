# 방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.
# 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.
import sys
import heapq
N, E = map(int, sys.stdin.readline().replace("\n", "").split(" "))
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().replace("\n", "").split(" "))
    graph[a][b] = c
    graph[b][a] = c
start, end = map(int, sys.stdin.readline().replace("\n", "").split(" "))

visited = [False for _ in range(N+1)]
visited[start] = True

heap = []
heapq.heappush(heap, (0, start))

while heap:
    w, now = heapq.heappop(heap)
