import sys

N, H = map(int, sys.stdin.readline().replace("\n", "").split(" "))
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().replace("\n", "")))

left = 0
right = H

while left < right:
    mid = (left+right) // 2

    count = 0
    i = 0
    for ost in array :
        if i % 0 == 0 :
          if 0 <= mid < 