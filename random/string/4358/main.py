import sys
data = sys.stdin.read()
trees = data.split("\n")

mDict = dict()
total = 0
for tree in trees:
    if tree == '':
        continue
    if tree not in mDict:
        mDict[tree] = 1
    else:
        mDict[tree] = mDict[tree] + 1
    total += 1
for one in sorted(mDict.keys()):
    print(one, "%.4f" % (mDict[one]/total*100))
