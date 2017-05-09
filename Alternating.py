
def alternating(ls):
    if not ls:
        return True
    elif len(ls)==1:
        return True
    else:
        if(ls[0]>ls[1]): 
            flag=1
            for e,i in enumerate(list(ls[:len(ls)-1])):
                up=i
                down=ls[e+1]
                if(flag==1):
                    flag=0
                    if(up<=down):
                        return False
                else:
                    flag=1
                    if(down<=up):
                        return False
            return True
        elif(ls[0]<ls[1]): 
            flag=1
            for e,i in enumerate(list(ls[:len(ls)-1])):
                down=i
                up=ls[e+1]
                if(flag==1):
                    flag=0
                    if(up<=down):
                        return False
                else:
                    flag=1
                    if(down<=up):
                        return False
            return True
        else:
            return False
print(alternating([1,3,2,3,1,3,1]))
print(alternating([5,1,4,2,4,3,5]))