import sys
N = int(sys.stdin.readline())
for _ in range(N):
    maxiam = 1
    a = sys.stdin.readline()
    array = list(map(int, sys.stdin.readline().split(' ')))
    candis = set(array)
    for candi in candis:
        maxiam = max(maxiam, array.count(candi))
    print(maxiam)
