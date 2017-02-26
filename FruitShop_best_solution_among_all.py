value = [int(x) for x in raw_input().split(" ")]

count = [int(x) for x in raw_input().split(" ")]

coin = int(raw_input())
lis = zip(value,count)
dic = dict(lis)
l=0;
for v in sorted(dic):
    c = dic[v]
    for i in range(0,c):
        if((coin-v)>=0):
            coin=coin-v
            #print coin
            l+=1
print l
