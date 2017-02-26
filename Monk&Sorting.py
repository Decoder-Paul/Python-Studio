from collections import defaultdict
def sort_algo(num,i,l):
    start = 5*(i-1)
    end = i*5
    n=len(num)
    weight=[]
    number=[]
    for item in num:
        number.append(int(item))
        if(start!=0):
            weight.append(int(item[-end:-start]))
        else:
            weight.append(int(item[-5:]))
    lis = zip(number,weight)
    print lis
    lis = sorted(lis,key=lambda x: x[1])
    for k,v in lis:
        print k, 
    l-=5
    if(l!=0):
        sort_algo(num,i+1,l)

def reSize(num,l):
    number=[]
    for item in num:
        newItem = str(item)
        newLength = l-len(newItem)
        for i in range(0,newLength):
            newItem='0'+newItem
        number.append(newItem)
    return number

n = int(raw_input())
num =[int(x) for x in raw_input().split(" ")]
maxOne = str(max(num))
l = len(maxOne)
r = l%5
if(r):
    l+=(5-r)
number=reSize(num,l)
#print number
sort_algo(number,1,l)
