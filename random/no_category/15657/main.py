import sys


def dfs(m, s, now, array, level):
    if m == level:
        answers = [array[i] for i in now]
        for answer in answers:
            print(answer, end=" ")
        print()
        return

    for i in range(s, len(array)):
        dfs(m, i, now+[i], array, level+1)


N, M = map(int, sys.stdin.readline().replace("\n", "").split())
array = list(map(int, sys.stdin.readline().replace("\n", "").split()))
array.sort()
now = []
dfs(M, 0, now, array, 0)
