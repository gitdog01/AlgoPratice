N = input()
Tmap = []
for _ in range(int(N)):
    Tmap.append(input().split(' '))
answer = []


def divide(x, y, n):

    counter = 0

    for i in range(y, y+n):
        for j in range(x, x+n):
            counter += int(Tmap[i][j])

    if counter == 0 or counter == n*n:
        answer.append('w' if counter == 0 else 'b')
        return

    divide(x, y, n//2)
    divide(x+n//2, y, n//2)
    divide(x, y+n//2, n//2)
    divide(x+n//2, y+n//2, n//2)


divide(0, 0, len(Tmap))
print(answer.count('w'))
print(answer.count('b'))
