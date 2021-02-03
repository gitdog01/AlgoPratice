import sys
N, limit = map(int, sys.stdin.readline().split(' '))
array = list(map(int, sys.stdin.readline().split(' ')))
array_sum = [0 for _ in range(N+1)]
temp_sum = 0
for idx, a in enumerate(array):
    temp_sum += a
    array_sum[idx+1] = temp_sum
line = 100001
start = 0
end = 1
while end < N+1:
    now_sum = array_sum[end]-array_sum[start]
    # print(now_sum)
    if now_sum < limit:
        end += 1
    elif now_sum > limit:
        line = min(line, end-start)
        #print(line, now_sum, end-start)
        start += 1
    else:
        line = min(line, end-start)
        #print(line, now_sum, end-start)
        end += 1
if line == 100001:
    print(0)
else:
    print(line)
