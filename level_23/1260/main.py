def dfs(arr, start):
    buf = [start]
    history = []
    while len(buf) != 0:
        now = buf.pop()
        if now not in history:
            history.append(now)
        arr[now].sort(reverse=True)
        for nextNode in arr[now]:
            if nextNode not in history:
                buf.append(nextNode)
    for a in history:
        print(a, end=' ')
    print()


def bfs(arr, start):
    buf = [start]
    history = []
    while len(buf) != 0:
        now = buf.pop(0)
        if now not in history:
            history.append(now)
        arr[now].sort()
        for nextNode in arr[now]:
            if nextNode not in history:
                buf.append(nextNode)
    for a in history:
        print(a, end=' ')
    print()


n, l, start = map(int, input().split(' '))
arr = [[] for _ in range(n+1)]
for _ in range(l):
    a, b = map(int, input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

dfs(arr, start)
bfs(arr, start)
