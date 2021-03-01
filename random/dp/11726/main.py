import sys
N = int(sys.stdin.readline().replace("\n", ""))
dp = [sys.maxsize for _ in range(N+1)]
if N > 2:
    dp[1] = 1
    dp[2] = 2

    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N] % 10007)
else:
    if N == 1:
        print(1)
    elif N == 2:
        print(2)
