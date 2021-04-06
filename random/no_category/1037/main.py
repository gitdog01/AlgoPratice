import sys
N = int(sys.stdin.readline().replace("\n", ""))
array = list(map(int, sys.stdin.readline().replace("\n", "").split()))
array.sort()
print(array[0]*array[-1])
