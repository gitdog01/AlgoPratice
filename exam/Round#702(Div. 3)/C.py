import sys
t = int(sys.stdin.readline().replace("\n", ""))


for _ in range(t):
    x = int(sys.stdin.readline().replace("\n", ""))
    start = 1
    end = 1
    answer = False

    while start < end:
        mid = (start+end) // 2
        big = start**3+end**3
        print(start, end, big)
        if x == big:
            answer = True
            break
        elif x > big:
            if x - big:
                start = mid + 1
        else:
            end = mid - 1
    if answer:
        print("YES")
    else:
        print("NO")
