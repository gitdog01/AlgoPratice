def check(mid, stones, k):
    ck = 0
    for i in stones:
        if i - mid <= 0:
            ck += 1
        else:
            ck = 0
        if ck >= k:
            return True
    return False


def solution(stones, k):
    MIN, MAX = 1, 200000000
    while MIN < MAX-1:
        mid = (MIN + MAX) // 2
        if check(mid, stones, k):
            MAX = mid
        else:
            MIN = mid
    return MAX
