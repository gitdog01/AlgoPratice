import sys
N, K = map(int, sys.stdin.readline().replace("\n", "").split())
coins = []

for _ in range(N):
    coins.append(int(sys.stdin.readline().replace("\n", "")))

dp = [0 for _ in range(K+1)]
dp[0] = 1

for i in coins:
    for j in range(i, K + 1):
        dp[j] += dp[j - i]

print(dp[K])
