import sys
N = int(sys.stdin.readline().replace("\n", ""))
array = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
answer = []
for i in range(1, min(array)+1):
    if N == 3:
        if array[0] % i == 0 and array[1] % i == 0 and array[2] % i == 0:
            answer.append(i)
    else:
        if array[0] % i == 0 and array[1] % i == 0:
            answer.append(i)

for one in answer:
    print(one)
