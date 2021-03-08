n, c = map(int, input().split(' '))
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
start = 1
end = arr[-1] - arr[0]

ans = 0
while start <= end:
    mid = (start + end) // 2
    d = 1
    last = arr[0]
    for idx in range(1, len(arr)):
        if arr[idx] >= last+mid:
            d += 1
            last = arr[idx]
    if d >= c:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)
