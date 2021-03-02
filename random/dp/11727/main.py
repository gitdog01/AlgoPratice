import sys
N = int(sys.stdin.readline().replace("\n", ""))
dp = [0 for _ in range(N+1)]
dp[1] = 1
dp[2] = 3
for i in range(3, N+1):
    for a in range(1, i):
        dp[i] += dp[i-a] + dp[a]

print(dp[N] % 10007)
