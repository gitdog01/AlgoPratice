import sys


def dfs(m, now, array, visited, level):
    if m == level:
        answers = [array[i] for i in now]
        for answer in answers:
            print(answer, end=" ")
        print()
        return

    for i in range(len(array)):
        if visited[i] == False:
            visited[i] = True
            dfs(m, now+[i], array, visited, level+1)
            visited[i] = False


N, M = map(int, sys.stdin.readline().replace("\n", "").split())
array = list(map(int, sys.stdin.readline().replace("\n", "").split()))
array.sort()
visited = [False for _ in range(N)]
now = []
dfs(M, now, array, visited, 0)
