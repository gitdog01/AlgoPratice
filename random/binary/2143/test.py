from collections import defaultdict
import sys
# 다른 사람의 코드와 속도를 비교해 보기 위해서 넣었습니다.
# 출처 : https://velog.io/@nyanyanyong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98python%EB%B0%B1%EC%A4%80-2143%EB%91%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%ED%95%A9
T = int(sys.stdin.readline())

a = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))
b = int(sys.stdin.readline())
listB = list(map(int, sys.stdin.readline().split()))

dictA = defaultdict(int)


answer = 0

for i in range(a):
    for j in range(i, a, 1):
        dictA[sum(listA[i:j+1])] += 1

for i in range(b):
    for j in range(i, b, 1):
        answer += dictA[T - sum(listB[i:j+1])]

print(answer)
