import sys
N = int(sys.stdin.readline().replace("\n", ""))
RANGE = 20
S = list('0'*RANGE)

for _ in range(N):
    command = sys.stdin.readline().replace("\n", "").split()
    if len(command) == 2:
        x = int(command[1])-1
    if command[0] == 'add':
        S[x] = '1'
    elif command[0] == 'check':
        print(S[x])
    elif command[0] == 'remove':
        S[x] = '0'
    elif command[0] == 'toggle':
        if S[x] == '0':
            S[x] = '1'
        else:
            S[x] = '0'
    elif command[0] == 'all':
        S = list('1'*RANGE)
    elif command[0] == 'empty':
        S = list('0'*RANGE)
