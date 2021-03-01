import sys
R = 0
G = 1
B = 2
N = int(sys.stdin.readline().replace("\n", ""))
array = [[0, 0, 0]]
dp = [[sys.maxsize for _ in range(3)]for _ in range(N+1)]
for _ in range(N):
    array.append(
        list(map(int, sys.stdin.readline().replace("\n", "").split(" "))))

dp[1][R] = array[1][R]  # 26
dp[1][G] = array[1][G]  # 40
dp[1][B] = array[1][B]  # 83

# R (G/B)
# G (R/B)
# B (R/G)

# i = 2 / 49 60 57
dp[2][R] = min(array[2][R]+dp[1][G], array[2][R]+dp[1][B])  # 49 + 40 / 49 + 83
dp[2][G] = min(array[2][G]+dp[1][R], array[2][G]+dp[1][B])  # 60 + 26 / 60 + 83
dp[2][B] = min(array[2][B]+dp[1][G], array[2][B]+dp[1][R])  # 57 + 40 / 57 + 26

# 1 R - (G/B) - (B/G) 4case
# 2 G - (R/B) - (B/R) 4case
# 3 B - (G/R) - (R/G) 4case

for i in range(3, N+1):
    case1 = array[i][R] + array[i-1][G] + dp[i-2][B]
    case2 = array[i][R] + array[i-1][G] + dp[i-2][R]
    case3 = array[i][R] + array[i-1][B] + dp[i-2][G]
    case4 = array[i][R] + array[i-1][B] + dp[i-2][R]

    dp[i][R] = min(case1, case2, case3, case4)

    case1 = array[i][G] + array[i-1][R] + dp[i-2][B]
    case2 = array[i][G] + array[i-1][R] + dp[i-2][G]
    case3 = array[i][G] + array[i-1][B] + dp[i-2][R]
    case4 = array[i][G] + array[i-1][B] + dp[i-2][G]

    dp[i][G] = min(case1, case2, case3, case4)

    case1 = array[i][B] + array[i-1][R] + dp[i-2][G]
    case2 = array[i][B] + array[i-1][R] + dp[i-2][B]
    case3 = array[i][B] + array[i-1][G] + dp[i-2][R]
    case4 = array[i][B] + array[i-1][G] + dp[i-2][B]

    dp[i][B] = min(case1, case2, case3, case4)

print(min(dp[N][R], dp[N][B], dp[N][G]))
