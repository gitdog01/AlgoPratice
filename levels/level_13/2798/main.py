Card_num,Target = input().split()
Cards = input().split()
near = 300000
for i in range(0,len(Cards)-2) :
    for j in range(i+1,len(Cards)-1) :
        for k in range(j+1,len(Cards)) :
            total = int(Cards[k]) + int(Cards[j]) + int(Cards[i])
            if abs(int(Target) - near) > abs(int(Target) - total) and int(Target) >= total:
                near = total
print(near)