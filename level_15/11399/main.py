N = int(input())
result = 0
previous = 0
priority = list(map(int, input().split(' ')))
priority.sort()

for num in priority:
    result += previous+num
    previous += num

print(result)
