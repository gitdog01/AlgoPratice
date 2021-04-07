def solve(n, stones, dp, left, right, level):
    poss = abs(left-right)
    if n == level:
        dp[level][poss] = "Y"
        return

    #print(level, "/", len(dp)-1, poss, "/", len(dp[0])-1)
    # print(dp)
    if dp[level][poss] == "N":

        solve(n, stones, dp, left+stones[level], right, level+1)
        solve(n, stones, dp, left, right+stones[level], level+1)
        solve(n, stones, dp, left, right, level+1)
        dp[level][poss] = "Y"


N = int(input())
stones = list(map(int, input().split()))
M = int(input())
answers = list(map(int, input().split()))
dp = [["N" for _ in range(sum(stones)+1)]for _ in range(N+1)]

solve(N, stones, dp, 0, 0, 0)
# print(dp)

for i in answers:
    if sum(stones) >= i:
        print(dp[N][i], end=" ")
    else:
        print("N", end=" ")
print()
