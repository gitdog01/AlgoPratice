import sys
N = int(sys.stdin.readline().replace("\n", ""))
i = 2
while N != 1:
    if N % i == 0:
        print(i)
        N = N // i
    else:
        i += 1
