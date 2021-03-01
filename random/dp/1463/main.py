import sys
N = int(input())
dp = [sys.maxsize for _ in range(N+1)]

if N > 0:
    dp[1] = 0
if N > 1:
    dp[2] = 1
if N > 2:
    dp[3] = 1

for i in range(4, N+1):
    a, b, c = sys.maxsize, sys.maxsize, sys.maxsize
    if i % 3 == 0:
        a = dp[i//3]+1
    if i % 2 == 0:
        b = dp[i//2]+1
    if i < N + 1:
        c = dp[i-1]+1
    dp[i] = min(a, b, c)
print(dp[N])
