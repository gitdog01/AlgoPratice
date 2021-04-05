N = int(input())
result = []
for _ in range(N):
    buf = input()
    time = 0
    combo = 0
    for word in buf:
        if word == 'O':
            time += 1 + combo
            combo += 1
        else:
            combo = 0
    result.append(time)

for line in result:
    print(line)
