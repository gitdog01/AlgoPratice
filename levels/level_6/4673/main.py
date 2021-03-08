def d(n):
    return n + sum([int(one) for one in str(n)])


numbers = [0 for _ in range(10000)]
for i in range(10000):
    if d(i) < 10000:
        numbers[d(i)] = 1

for i in range(10000):
    if numbers[i] == 0:
        print(i)
