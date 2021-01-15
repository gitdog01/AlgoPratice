n = int(input())
arr = list(map(int, input().split(' ')))
result = [0 for _ in range(n)]
for idx in range(len(arr)):
    result[idx] = max(result[idx-1] + arr[idx], arr[idx])
print(max(result))
