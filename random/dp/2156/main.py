# 768
import sys
N = int(sys.stdin.readline().replace("\n", ""))
array = [0]
dp = [0 for _ in range(N+1)]
for _ in range(N):
    array.append(int(sys.stdin.readline().replace("\n", "")))
if N > 3:

    dp[1] = max([array[1]])
    dp[2] = max([dp[1]+array[2], array[2]])
    dp[3] = max([array[1]+array[2], array[2]+array[3], array[1]+array[3]])

    # 1 X O O X ~
    # 2 O X O O ~
    # 3 O O X O ~
    for i in range(4, N+1):
        case1 = array[i-1] + array[i-2] + dp[i-4]
        case2 = array[i] + dp[i-2]
        case3 = array[i] + array[i-1] + dp[i-3]
        dp[i] = max([case1, case2, case3])

    print(dp[N])
else:
    if N == 1:
        print(array[1])
    if N == 2:
        print(array[1]+array[2])
    if N == 3:
        print(max([array[1]+array[2], array[1]+array[3], array[2]+array[3]]))
