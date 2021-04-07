import sys
N, K = map(int, sys.stdin.readline().replace("\n", "").split())
coins = []

for _ in range(N):
    coins.append(int(sys.stdin.readline().replace("\n", "")))


dp = [[] for _ in range(2)]
dp[0] = [[0 for _ in range(N)]]
while dp[0]:
    dp[1] = []
    for one in dp[0]:
        print("one", one)
        total = 0
        for a in range(len(one)):
            total += one[a] * coins[a]
        print("total", total)
        if total > K:
            break

        for i in range(N):
            one[i] += 1
            dp[1].append(one[:])
            one[i] -= 1
    dp[0] = list(set(dp[1][:]))
    print(dp)
