x = input("Enter: ").split()
d = {}
for i in range(len(x)):
    n = ''.join(sorted(x[i]))
    if n not in d:
        d[n] = [x[i]]
    else:
        d[n].append(x[i])
print(d)