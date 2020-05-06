def divide_num(num) :
    total = int(num)
    for i in num :
        total += int(i)
    return total

n = input()
for j in range(1,int(n)+1) :
    if divide_num(str(j)) == int(n) :
        print(j)
        break
    if j == int(n) :
        print(0)
        break
