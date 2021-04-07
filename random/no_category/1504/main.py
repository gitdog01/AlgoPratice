import sys
N, E = map(int, sys.stdin.readline().replace("\n", "").split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().replace("\n", "").split())
    graph[a][b] = c
    graph[b][a] = c
start, end = map(int, sys.stdin.readline().replace("\n", "").split())
answer = sys.maxsize


for i in range(1, len(graph[start])):
    if graph[start][i] == 0 or start == i or end == i:
        continue
    for j in range(1, len(graph[i])):
        if graph[i][j] == 0 or start == j or end == j:
            continue
        if graph[j][end] == 0:
            continue
        print(i, j, graph[start][i], graph[i][j], graph[j][end])
        answer = min(answer, graph[start][i] + graph[i][j] + graph[j][end])

for one in graph:
    print(one)
print(answer)
