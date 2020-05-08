N = int(input())

t_list = []
booked = []


for a in range(N) :
    temp = input().split(" ")
    temp2 = [temp,abs(int(temp[0])-int(temp[1]))]
    t_list.append(temp2)

print(t_list)