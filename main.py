a = 1
print(id(a))
f_add = id(a)
a += 1
print(id(a))
s_add = id(a)
print(f_add is s_add)
