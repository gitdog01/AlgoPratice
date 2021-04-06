import sys
N = int(sys.stdin.readline().replace("\n", ""))
A = list(map(int, sys.stdin.readline().replace("\n", "").split()))
P = [-1 for _ in range(0, N)]
B = sorted(A)
for i in range(N):
    num = B.index(A[i])
    P[i] = num
    B[num] = -1


for one in P:
    print(one, end=" ")
print()
