buf = input().split('-')
result = 0
for one in buf[0].split('+'):
    result += int(one)
for i in range(1, len(buf)):
    task = buf[i].split('+')
    line = 0
    for one in task:
        line += int(one)
    result -= line
print(result)
