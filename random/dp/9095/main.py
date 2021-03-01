import sys
T = int(sys.stdin.readline().replace("\n", ""))
for _ in range(T):
    N = int(sys.stdin.readline().replace("\n", ""))
    dp = [sys.maxsize for _ in range(N+1)]
    if N > 3:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

        for i in range(4, N+1):
            dp[i] = (dp[i-1]) + (dp[i-2]) + (dp[i-3])

        print(dp[N])
    else:
        if N == 1:
            print(1)
        elif N == 2:
            print(2)
        elif N == 3:
            print(4)
