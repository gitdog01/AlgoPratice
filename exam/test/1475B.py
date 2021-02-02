import sys
T = int(sys.stdin.readline())
for _ in range(T):
    num = int(sys.stdin.readline())
    remain = num // 2020
    if (remain*2020) <= num <= (remain*2021):
        print("YES")
    else:
        print("NO")
