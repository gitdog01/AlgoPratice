import sys
N = int(sys.stdin.readline().replace("\n", ""))
A = [0 for _ in range(N)]
X = [0 for _ in range(N)]
for idx in range(N):
    X[idx], A[idx] = map(
        int, sys.stdin.readline().replace("\n", "").split(" "))
start = 0
end = N - 1
mini = sys.maxsize

while start <= end:
    mid = (start+end)//2

    temp = 0
    for i in range(N):
        temp += abs(X[i]-mid)*A[i]
    print("d", temp, "mid", mid)
    if temp < mini:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer+1)
