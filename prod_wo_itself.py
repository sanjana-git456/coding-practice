x = list(map(int, input("Enter: ").split()))
def prod(x):
    r = 1
    left = [1] * len(x)
    right = [1] * len(x)
    for i in range(len(x)):
        left[i] = r
        r *= x[i]
    r = 1
    for i in range(len(x)-1, -1, -1):
        right[i] = r
        r *= x[i]
    ans = [1] * len(x)
    for i in range(len(x)):
        ans[i] = left[i] * right[i]
    return ans
print(prod(x))