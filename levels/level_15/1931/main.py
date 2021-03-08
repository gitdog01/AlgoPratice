# 30분 넘김
time = []
N = int(input())
for _ in range(N):
    a, b = map(int, input().split(' '))
    time.append([a, b])
time.sort(key=lambda x: (x[1], x[0]))

endtime = time[0][1]
cnt = 1

for i in range(1, len(time)):
    if time[i][0] >= endtime:
        cnt += 1
        endtime = time[i][1]
print(cnt)
