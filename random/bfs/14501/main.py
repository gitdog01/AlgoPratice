import sys
N = int(sys.stdin.readline().replace("\n", ""))
dp = [0 for _ in range(N+6)]
time = []
pay = []
for _ in range(N):
    T, P = map(int, sys.stdin.readline().replace("\n", "").split(" "))
    time.append(T)
    pay.append(P)

for i in range(N-1, -1, -1):
    # 6
    if time[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], pay[i]+dp[i+time[i]])
    # print(dp)

print(dp[0])
