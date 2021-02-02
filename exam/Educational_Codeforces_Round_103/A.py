import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split(' '))
    if n > k:
        a = 1 * n
        high = 1
    else:
        start = k // n
        a = start * n
        high = start
    idx = n
    while a % k != 0:
        a += 1
        if idx < n - 1:
            idx = idx+1
        else:
            idx = 0
            high += 1
    print(high)
