import sys
M = int(sys.stdin.readline().replace("\n", ""))
N = int(sys.stdin.readline().replace("\n", ""))


def prime_list(n, bottom):
    n += 1
    prime = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        for j in range(i+i, n, i):
            prime[j] = False
    prime[1] = False
    return [i for i in range(bottom, n) if prime[i]]


prime = prime_list(N, M)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])
