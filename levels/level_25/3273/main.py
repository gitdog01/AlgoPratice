x = int(input())
a = list(map(int, input().split(' ')))
a.sort()
n = int(input())
i = 0
j = x-1
count = 0
while i < j:
    if a[i] + a[j] < n:
        i += 1
    elif a[i] + a[j] > n:
        j -= 1
    elif a[i] + a[j] == n:
        count += 1
        j -= 1


print(count)
