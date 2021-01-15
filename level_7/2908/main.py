a, b = input().split(' ')
inta = int(a[::-1])
intb = int(b[::-1])
if inta > intb:
    print(inta)
else:
    print(intb)
