import sys

N = int(sys.stdin.readline().replace("\n", ""))

max_dp = [[0 for _ in range(3)] for _ in range(2)]
min_dp = [[0 for _ in range(3)] for _ in range(2)]

for y in range(N):
    line = list(map(int, sys.stdin.readline().replace("\n", "").split()))
    for x in range(3):
        if x == 0:
            max_dp[1][0] = max(line[0] + max_dp[0][0],
                               line[0] + max_dp[0][1])
            min_dp[1][0] = min(line[0] + min_dp[0][0],
                               line[0] + min_dp[0][1])
        elif x == 1:
            max_dp[1][1] = max(line[1] + max_dp[0][0],
                               line[1] + max_dp[0][1],
                               line[1] + max_dp[0][2])
            min_dp[1][1] = min(line[1] + min_dp[0][0],
                               line[1] + min_dp[0][1],
                               line[1] + min_dp[0][2])
        elif x == 2:
            max_dp[1][2] = max(line[2] + max_dp[0][1],
                               line[2] + max_dp[0][2])
            min_dp[1][2] = min(line[2] + min_dp[0][1],
                               line[2] + min_dp[0][2])
    max_dp[0] = max_dp[1][:]
    min_dp[0] = min_dp[1][:]

print(max(max_dp[0]), min(min_dp[0]))

# 4 5 6
# 7 8 9
