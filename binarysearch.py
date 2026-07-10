x = list(map(int, input("Enter: ").split()))
t = int(input("Enter target: "))
def binary(x,t):
    low = 0
    high = len(x) - 1
    while low <= high:
        mid = (low+high) // 2
        if t == x[mid]:
            return mid
        elif t < x[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
print(binary(x,t))