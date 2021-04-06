import sys

N = int(sys.stdin.readline().replace("\n", ""))
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().replace("\n", "")))
answers = []
for i in range(2, max(array)):
    l = None
    flag = True
    for num in array:
        if l == None:
            l = num % i
        else:
            if l != num % i:
                flag = False
                break
    if flag:
        answers.append(i)
for one in answers:
    print(one, end=' ')
print()
