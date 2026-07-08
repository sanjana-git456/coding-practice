x = list(map(int, input("Enter: ").split()))
t = int(input("Enter target: "))
def twosum(x,t):
    l = 0
    r = len(x) - 1
    while l < r:
        if x[l] + x[r] == t:
            return l,r
        elif x[l] + x[r] < t:
            l += 1
        else:
            r -= 1
    return -1
print(twosum(x,t))