#main.py
max_order = int(0)
max_number = int(0)
for n in range(0,9) :
    number = int(input())
    if max_number < number :
        max_number = number
        max_order  = n + 1
print(max_number)
print(max_order)
