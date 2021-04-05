import sys


def dfs(num, array):
    array[num] = -2
    for i in range(len(array)):
        if num == array[i]:
            dfs(i, array)


N = int(sys.stdin.readline().replace("\n", ""))
array = list(map(int, sys.stdin.readline().replace("\n", "").split()))
k = int(sys.stdin.readline().replace("\n", ""))

dfs(k, array)
count = 0
for i in range(len(array)):
    if array[i] != -2 and i not in array:
        count += 1
print(count)
