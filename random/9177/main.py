import sys


T = int(sys.stdin.readline().replace("\n", ""))
for i in range(T):
    first, second, third = map(
        list, sys.stdin.readline().replace("\n", "").split(" "))

    def dfs(one, two, three):
        answer = 0
        if three == len(third):
            return 1
        if one < len(first) and first[one] == third[three]:
            answer += dfs(one+1, two, three+1)
        if two < len(second) and second[two] == third[three]:
            answer += dfs(one, two+1, three+1)
        return answer

    if dfs(0, 0, 0, '') > 0:
        print("Data set %d: yes" % (i+1))
    else:
        print("Data set %d: no" % (i+1))
