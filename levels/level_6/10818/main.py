#main.py
n = int(input())
number_list = input().split(" ")
max = int(number_list[0])
min = int(number_list[0])
for number in number_list :
    if max < int(number) :
        max = int(number)
    if min > int(number) :
        min = int(number)
print(min,max)
