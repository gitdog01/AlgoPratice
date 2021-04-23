import sys
N = int(sys.stdin.readline().replace("\n", ""))
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().replace("\n", "")))
array.sort(reverse=True)
# print(array)
answer = 0
# plus
i = 0
save = 0
while len(array) > i and array[i] > 0:
    if array[i] == 1:
        answer += 1 + save
        save = 0
    elif save == 0:
        save = array[i]
    else:
        answer += save*array[i]
        save = 0
    i += 1
if save > 0:
    answer += save

# minus
i = len(array)-1
save = 1
while i > -1 and array[i] <= 0:
    if save == 1:
        save = array[i]
    else:
        answer += save*array[i]
        save = 1
    i -= 1
if save != 1:
    answer += save

print(answer)
