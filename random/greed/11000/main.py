import sys
N = int(sys.stdin.readline().replace("\n", ""))
S = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().replace("\n", "").split())
    S.append([a, b, b-a])
S.sort(key=lambda x: x[2])
S.sort(key=lambda x: x[0])
last_start = 0
last_end = 0
answer = 0
for i in range(len(S)):
    now = S[i]
    if last_end < now[0]:
        answer += 1
        last_end = now[1]
print(answer)
