n = int(input())
for _ in range(n):
    x, word = input().split(' ')
    for chartter in word:
        print(chartter*int(x), end='')
    print()
