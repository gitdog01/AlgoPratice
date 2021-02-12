import sys
N = int(sys.stdin.readline().replace("\n", ""))
array = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
array.sort()

mini = sys.maxsize
answer = []
for idx in range(len(array)):
    left = idx + 1
    right = len(array) - 1
    breaker = False
    while left < right:
        pivate = array[idx] + array[left] + array[right]

        if abs(pivate) < mini:
            mini = abs(pivate)
            answer = [array[idx], array[left], array[right]]

        if pivate == 0:
            answer = [array[idx], array[left], array[right]]
            breaker = True
            break
        elif pivate < 0:
            left += 1
        elif pivate > 0:
            right -= 1

    if breaker == True:
        break
for a in answer:
    print(a, sep=' ')
print()
