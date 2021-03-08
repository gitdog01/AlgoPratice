n = int(input())
for _ in range(n):
    arr = list(map(int, input().split(' ')))
    num = arr[0]
    numbers = arr[1:]
    avg = sum(numbers)/num
    count = 0
    for temp in numbers:
        if temp > avg:
            count += 1
    print('%.3f%%' % (count/len(numbers)*100))
