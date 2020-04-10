#main.py
h,m = input().split()
h = int(h)
m = int(m)
if m < 45 :
    r = m - 45
    if h == 0 :
        h = 23
    else :
        h = h - 1
    m = 60 + r
    print(h,m)
else :
    print(h,(m-45))