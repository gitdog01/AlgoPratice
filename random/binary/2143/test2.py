import sys
dictA = dict()

dictA[0] = 1
dictA[sys.maxsize] = 1
dictA[10*sys.maxsize+1] = 1

print(dictA[0])
print(dictA[sys.maxsize])
print(dictA[10*sys.maxsize+1])
