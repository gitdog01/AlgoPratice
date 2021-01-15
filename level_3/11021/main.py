n = int(input())

for idx in range(1, n+1):
    a, b = map(int, input().split(' '))
    print('Case #'+str(idx)+':', a+b)
