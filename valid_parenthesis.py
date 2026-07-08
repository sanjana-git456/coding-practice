x = input("Enter: ")
l = []
d = {')' : '(' , ']' : '[' , '}' : '{'}
def parenthesis(x,l,d):
    for i in x:
        if i not in d:
            l.append(i)
        elif i in d:
            if not l or l[-1] != d[i]:
                return False
            l.pop()
        else:
            return False
    if l == []:
        return True
print(parenthesis(x,l,d))