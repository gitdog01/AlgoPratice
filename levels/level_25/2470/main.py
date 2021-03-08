import re
n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()
start = 0
end = n - 1
closer = arr[start] + arr[end]
while start < end:
    if arr[start] + arr[end] < closer:
        print('save')


new_id = 'a'
new_id.replace
