import sys
N = int(sys.stdin.readline().replace("\n", ""))
R = int(sys.stdin.readline().replace("\n", ""))
array = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
image = {}

for i in range(len(array)):
    if array[i] not in image:
        if len(image) < N:
            image[array[i]] = [1, i]
        else:
            del_list = sorted(image.items(), key=lambda x: (x[1][0], x[1][1]))
            del_key = del_list[0][0]
            del(image[del_key])
            image[array[i]] = [1, i]
    else:
        image[array[i]] = [image[array[i]][0]+1, image[array[i]][1]]


ans_list = list(sorted(image.keys()))
for a in ans_list:
    print(a, end=" ")
print()
