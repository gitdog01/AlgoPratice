import sys
N = int(sys.stdin.readline().replace("\n", ""))
triangle = [[]]
dp = [[] for _ in range(N+1)]
for _ in range(N):
    triangle.append(
        list(map(int, sys.stdin.readline().replace("\n", "").split(" "))))
dp[1] = [triangle[1][0]]  # 7
dp[2] = [triangle[2][0]+triangle[1][0], triangle[2][1]+triangle[1][0]]  # [10 , 15]
for i in range(3, N+1):
    dp[i] = [0 for _ in range(len(triangle[i]))]
    for j in range(len(triangle[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]  # [3][0] = [2][0] + [3][0]
        elif j == len(triangle[i])-1:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            case1 = dp[i-1][j-1] + triangle[i][j]
            case2 = dp[i-1][j] + triangle[i][j]
            dp[i][j] = max(case1, case2)
print(max(dp[N]))
