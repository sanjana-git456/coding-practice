x = input("Enter: ")
y = input("Enter: ")
def anagram(x,y):
    x = sorted(x)
    y = sorted(y)
    if x == y:
        return True
    else:
        return False
print(anagram(x,y))