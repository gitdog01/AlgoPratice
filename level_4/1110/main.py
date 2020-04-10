#main.py
a = input()
c = "-"
n = int(0)
if int(a) < 10 :
    a = "0" + a
b = int(a[0]) + int(a[1])
c = a[1] + str(b%10)
n += 1

while a!=c :
    b = int(c[0]) + int(c[1])
    c = c[1] + str(b%10)
    n += 1
print(n)
