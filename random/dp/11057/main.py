import sys
N = int(sys.stdin.readline().replace("\n", ""))
dp = [[0 for i in range(10)] for _ in range(N+1)]


for i in range(10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(0, 10):
        for k in range(0, j+1):
            dp[i][j] += dp[i-1][k]

total = 0
for one in dp[N]:
    total += one
print(total % 10007)
