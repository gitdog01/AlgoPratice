n = int(input())
scores = list(map(int, input().split(' ')))
m = max(scores)
avg = 0
for num in scores:
    avg += num/m*100
print(avg/len(scores))
