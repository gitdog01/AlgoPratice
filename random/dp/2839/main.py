import sys
N = int(sys.stdin.readline().replace("\n", ""))
answer = 0
dp = [[] for _ in range(N//3+1)]
dp[0] = [0]
breaker = False
while min(dp[answer]) < N:
    for a in dp[answer]:
        three = a+3
        five = a+5
        if three == N or five == N:
            print(answer+1)
            breaker = True
            break
        dp[answer+1].append(a+3)
        dp[answer+1].append(a+5)
    if breaker:
        break
    answer += 1
    dp[answer] = list(set(dp[answer]))
if not breaker:
    print(-1)
