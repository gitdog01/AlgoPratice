import sys
import collections


def solve(road, n):
    count = 0
    myroad = []
    temp = 0

    for one in road:

        if one == "1":
            count += 1
        else:
            if count != 0:
                myroad.append(count)
                myroad.append(-1)
                count = 0
            else:
                myroad.append(-1)
    if count > 0:
        myroad.append(count)

    print(myroad)

    m = 0
    answer = 0
    candi = collections.deque([])
    for idx in range(len(myroad)):

        if myroad[idx] == -1:
            candi.append(idx)
            m += 1
            # my road
            if m > n:
                candi.popleft()
                m -= 1
        if len(candi) == 0:
            continue
        now = 0  # sum
        if candi[0] > 0 and myroad[candi[0]-1] > 0:
            now += myroad[candi[0]-1]
        for i in candi:
            if i+1 < len(myroad) and myroad[i+1] > 0:
                now += myroad[i+1]
        now += len(candi)
        answer = max(answer, now)

    return answer


road = input()
n = int(input())

print(solve(road, n))
