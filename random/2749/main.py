import sys
N = int(sys.stdin.readline().replace("\n", ""))


a, b = 0, 1
N = N % (15*100000)
for i in range(N):
    a, b = b % 1000000, (a+b) % 1000000
print(a)
