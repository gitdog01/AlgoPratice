#main.py
a = int(input())
if (a % 4) == 0 :
    if not ( a % 100 ) == 0 or ( a % 400 ) == 0 :
        print(1)
    else :
        print(0)
else :
    print(0) 