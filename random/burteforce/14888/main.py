import sys


N = int(sys.stdin.readline().replace("\n", ""))
array = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
plus, minus, multi, nanu = list(map(
    int, sys.stdin.readline().replace("\n", "").split(" ")))
maxv = -sys.maxsize
minv = sys.maxsize


def cal(pre, idx, array, p, m, x, n):
    global N, maxv, minv
    if idx == N:
        maxv = max(maxv, pre)
        minv = min(minv, pre)
        return
    if p > 0:
        cal(pre+array[idx], idx+1, array, p-1, m, x, n)
    if m > 0:
        cal(pre-array[idx], idx+1, array, p, m-1, x, n)
    if x > 0:
        cal(pre*array[idx], idx+1, array, p, m, x-1, n)
    if n > 0:
        cal(int(pre/array[idx]), idx+1, array, p, m, x, n-1)


cal(array[0], 1, array, plus, minus, multi, nanu)
print(maxv)
print(minv)
