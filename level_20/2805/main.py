n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr.sort()
start = 0
end = max(arr)
mid = 0
last = 0
ans = 0
while start <= end:

    mid = (start + end) // 2
    last = 0
    for one in arr:
        if one - mid > 0:
            last += one - mid
    if last >= k:
        ans = mid
        start = mid + 1
    elif last < k:
        end = mid - 1
print(ans)
