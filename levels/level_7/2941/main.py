croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
line = input()
for alpha in croatia:
    line = line.replace(alpha, '#')
print(len(line))
