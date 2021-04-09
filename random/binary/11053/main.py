import sys
N = int(sys.stdin.readline().replace("\n", ""))
array = list(map(int, sys.stdin.readline().replace("\n", "").split()))
dp = [False for _ in range(N)]

for i in range(N):
    count = 0
    for j in range(i):
        if array[i] > array[j]:
            count = max(count, dp[j])
    dp[i] = count + 1
print(max(dp))
