def binarySearch(f, numbers):
    start = 0
    end = len(numbers)-1
    if numbers[start] > f:
        return 0
    elif numbers[end] < f:
        return 0
    # 아웃
    while start != end:
        r = (start+end) // 2
        if numbers[start] == f:
            return 1
        elif numbers[end] == f:
            return 1

        if numbers[r] == f:
            return 1
        elif numbers[r] > f:
            end = r
        elif numbers[r] < f:
            start = r

        if abs(start-end) == 1:
            return 0
    return 0


# 1 2 3 4 6
n = input()
numbers = list(map(int, input().split(' ')))
numbers.sort()
m = input()
finder = list(map(int, input().split(' ')))

for f in finder:
    print(binarySearch(f, numbers))
