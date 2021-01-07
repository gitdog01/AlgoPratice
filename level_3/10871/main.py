n, max = map(int, input().split(' '))
array = input().split(' ')
result = []
for a in array:
    if max > int(a):
        result.append(a)
for b in result:
    print(b, end=' ')
