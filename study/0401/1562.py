import sys


def solve(N):
    if N < 10:
        return 0

    dp = [[0 for _ in range(10)] for _ in range(2)]
# 꺽는 수

# 10 일때 1개

# 11 일때는 dp[10][9] + 1 = dp[11][8] = 1
# 11 일때는 1 + dp[10][9] = dp[11][9] = 1
# 11 일때 2개

# 12 일때는 dp[11][8] + 2 = dp[12][9] = 1
#                        =  dp[12][7] = 1
# 12 일때는 1 + dp[11][8] = dp[12][8] = 1
#

    for i in range(1, 10):
        dp[1][i] = 1

    for n in range(10, N+1):
        dp[n] = 0


N = int(sys.stdin.readline().replace("\n", ""))
print(solve(N))
