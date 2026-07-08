x = list(map(int, input("Enter: ").split()))
t = int(input("Enter target: "))
d = {}
for i in range(len(x)):
    a = t - x[i]
    if a in d:
        print(d[a], i)
    d[x[i]] = i