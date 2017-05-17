def matched(symbolString):
    index = 0
    a=0
    l=[]
    while index < len(symbolString):
        symbol = symbolString[index]
        if symbol == "(":
            l.append("(")
        elif symbol== ")" and len(l)!=0:
            l.pop()
        index = index + 1
    if len(l)==0:
        return True
    else:
        return False
print(matched("zb%78"))
print(matched("(7)(a"))
print(matched("a)*(?"))
print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))