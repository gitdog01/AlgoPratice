import sys
N, M = map(int, sys.stdin.readline().split(' '))
a = {}
visited = [True] + [False for _ in range(N)]
for i in range(N):
    a[i+1] = []
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split(' '))
    a[i].append(j)
    a[j].append(i)

stack = []
answer = 0
while visited.count(False) != 0:
    stack.append(visited.index(False))
    while stack:
        now = stack.pop()
        visited[now] = True
        for next in a[now]:
            if visited[next] != True:
                stack.append(next)
                visited[next] = True
        # print(now, stack)
    answer += 1
print(answer)
