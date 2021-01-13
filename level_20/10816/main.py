n = input()
numbers = list(map(int, input().split(' ')))
numbers.sort()
m = input()
finder = list(map(int, input().split(' ')))

for f in finder:
    print(numbers.count(f), end=' ')
