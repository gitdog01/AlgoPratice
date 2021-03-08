import sys
input = int(sys.stdin.readline().rstrip())
for _ in range(input):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    print(a+b)
