import sys
t = int(sys.stdin.readline().replace("\n", ""))


def dense(a, b):
    if max(a, b) // min(a, b) <= 2:
        return True
    else:
        return False


answers = []

for _ in range(t):
    answer = 0
    n = int(sys.stdin.readline().replace("\n", ""))
    array = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))

    for i in range(0, len(array)-1):
        temp = array[i]
        temp2 = array[i+1]
        while not dense(temp, temp2):
            answer += 1
            # print("ans ", temp, temp2)
            if temp > temp2:
                temp2 = temp2 * 2
            else:
                temp = temp * 2
            # print("bns ", temp, temp2)
    answers.append(answer)
for one in answers:
    print(one)
