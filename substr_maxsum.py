x = list(map(int, input("Enter: ").split()))
k = int(input("Enter k: "))
s = sum(x[0:k])
maximum = s
for i in range(k,len(x)):
    s = s - x[i-k] + x[i]
    maximum = max(s, maximum)
print(maximum)