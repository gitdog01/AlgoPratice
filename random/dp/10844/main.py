import sys
N = int(sys.stdin.readline().replace("\n", ""))
dp = [[0 for _ in range(10)] for _ in range(N+1)]
for n in range(1, 10):
    dp[1][n] = 1

for i in range(2, N+1):
    for l in range(0, 10):
        if l-1 > -1:
            case1 = dp[i-1][l-1]
        else:
            case1 = 0
        if l+1 < 10:
            case2 = dp[i-1][l+1]
        else:
            case2 = 0
        dp[i][l] = case1 + case2
print(sum(dp[N]) % 1000000000)
