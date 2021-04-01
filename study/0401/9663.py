import sys


def queen(board, n, level):
    count = 0
    if n == level:
        return 1
    for x in range(n):
        board[level] = x
        for i in range(level):
            if board[i] == board[level]:
                break
            if abs(board[i]-board[level]) == level - i:
                break
        else:
            count += queen(board, n, level+1)
    return count


N = int(sys.stdin.readline().replace("\n", ""))

board = [0 for _ in range(N)]
print(queen(board, N, 0))
