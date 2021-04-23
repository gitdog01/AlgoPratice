import sys
N = int(sys.stdin.readline().replace("\n", ""))

mDic = {}
w = []
for _ in range(N):
    words = list(sys.stdin.readline().replace("\n", ""))
    w.append(words)
    for i in range(len(words)):
        if words[i] not in mDic:
            mDic[words[i]] = 0
        mDic[words[i]] += 10 ** (len(words)-i)
greed = sorted(mDic.items(), key=lambda x: x[1], reverse=True)
nDic = {}
i = 9
for key, value in greed:
    nDic[key] = i
    i -= 1
answer = 0
for one in w:
    temp = ""
    for num in one:
        temp += str(nDic[num])
    answer += int(temp)
print(answer)
