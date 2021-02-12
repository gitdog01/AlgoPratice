import sys
N, M = map(int, sys.stdin.readline().replace("\n", "").split(" "))
array = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
answer = sys.maxsize
start = 0
end = sum(array)
head = max(array)
while start <= end:
    mid = (start+end)//2
    temp = 1
    temp_sum = 0
    if head > mid:
        start = mid + 1
        continue
    for one in array:
        temp_sum += one
        if temp_sum > mid:
            temp += 1
            temp_sum = one
    if temp > M:
        start = mid + 1
    else:
        answer = min(answer, mid)
        end = mid - 1
print(answer)
