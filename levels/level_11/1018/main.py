import sys
A, B = map(int, sys.stdin.readline().split(' '))
board = []
for _ in range(A):
    board.append(list(sys.stdin.readline()))

bw_count = 0
wb_count = 0
odd = 1
for line in board:
    for word in line:
        if odd == 1:
            bw_count += 1 if word == 'W' else 0
            wb_count += 1 if word == 'B' else 0
            odd *= -1
        else:
            bw_count += 1 if word == 'B' else 0
            wb_count += 1 if word == 'W' else 0
            odd *= -1
print(bw_count, wb_count)
print(min(bw_count, wb_count))
