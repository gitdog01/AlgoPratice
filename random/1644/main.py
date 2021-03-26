import sys


def prime_list(n):
    sieve = [True] * (n+1)

    m = int(n**0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i] == True]


N = int(sys.stdin.readline().replace("\n", ""))
p_list = prime_list(N)
answer = 0
total = 0
last = len(p_list)-1
for i in range(len(p_list)-1, -1, -1):
    total += p_list[i]

    while total > N:
        total -= p_list[last]
        last -= 1

    if total == N:
        answer += 1
        # print("[%d..%d]" % (p_list[i], p_list[last]))
print(answer)
