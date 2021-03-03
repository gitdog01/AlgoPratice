import sys
T = int(sys.stdin.readline().replace("\n", ""))
# 다시
answers = []
for _ in range(T):
    n = int(sys.stdin.readline().replace("\n", ""))
    a = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
    dp = []
    for i in range(n):
        now = i + a[i]
        if now > n:
            continue
        dp[now] = max(dp[i]+a[now], dp[now])
    # answers.append(max(dp))
    answers.append(max(dp))
    # print(dp)
for answer in answers:
    print(answer)
