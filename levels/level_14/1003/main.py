c0 = [1, 0, 1]
c1 = [0, 1, 1]

for i in range(3, 41):
    c0.append(c0[i-1]+c0[i-2])
    c1.append(c1[i-1]+c1[i-2])

for _ in range(int(input())):
    n = int(input())
    print(c0[n], c1[n])
