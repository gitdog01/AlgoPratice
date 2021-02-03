import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split(' ')))
array.sort()
left = 0
right = N-1
answer = 2000000001
answer_point = [left, right]
while left < right:
    pivet = array[left]+array[right]
    if abs(pivet) < answer:
        answer = abs(pivet)
        answer_point = [left, right]
    if pivet == 0:
        answer_point = [left, right]
        break
    elif pivet > 0:
        right -= 1
    elif pivet < 0:
        left += 1
print(array[answer_point[0]], array[answer_point[1]])
