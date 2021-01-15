T = int(input())
count = 0
last = ''
for _ in range(T):
    word = input()
    dc = 1
    history = []
    for alpha in word:
        if alpha not in history:
            history.append(alpha)
            last = alpha
        else:
            if last == alpha:
                continue
            else:
                dc = 0
                break
    count += dc
print(count)
