import sys
N, M = map(int, sys.stdin.readline().replace("\n", "").split(" "))
times = [0 for _ in range(N)]
for idx in range(N):
    times[idx] = int(sys.stdin.readline().replace("\n", ""))

start = 1
end = max(times) * M
answer = sys.maxsize

while start <= end:
    mid = (start+end)//2

    temp = 0

    for time in times:
        temp += mid//time

    if temp >= M:
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1

print(answer)
