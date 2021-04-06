import sys
N = int(sys.stdin.readline().replace("\n", ""))
count = 0
for i in range(5, N+1):
    while i % 5 == 0:
        i = i // 5
        count += 1
print(count)
