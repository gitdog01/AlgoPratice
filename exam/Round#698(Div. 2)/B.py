import sys
N = int(sys.stdin.readline())

for _ in range(N):
    candi = [False for _ in range(10001)]

    def finding(n, target, results, s):
        candi[n] = True
        for idx in range(s, len(results)):
            if n + results[idx] <= target:
                finding(n + results[idx], target, results, idx)
            else:
                return
    q, d = map(int, sys.stdin.readline().split(' '))
    a = list(map(int, sys.stdin.readline().split(' ')))
    decimal = [i for i in range(d, 10000, 10)]
    first = [i*d % 10 for i in range(1, 11)]
    maxiam = 10000
    newList = [x for x in decimal if x <= maxiam]
    finding(0, maxiam, newList, 0)
    for an in a:
        if candi[an]:
            print('YES')
        else:
            print('NO')
