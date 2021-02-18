import sys
import itertools
N = sys.stdin.readline().replace("\n", "")
array = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
permu = [i for i in range(len(array))]
maxv = - sys.maxsize
candi = set(itertools.permutations(permu, len(array)))

for now in candi:
    temp = []
    for idx in now:
        temp.append(array[idx])
    result = 0
    for idx in range(len(temp)-1):
        result += abs(temp[idx] - temp[idx+1])

    maxv = max(maxv, result)
print(maxv)
