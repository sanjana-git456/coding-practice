x = list(map(int, input("Enter: ").split()))
def dup(x):
    seen = set()
    for i in x:
        if i in seen:
            return True
        seen.add(i)
    return False
print(dup(x))