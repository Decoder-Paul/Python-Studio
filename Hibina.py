n=int(raw_input())
arr=[0]*6
for i in range(0,n):
	s_input=[x for x in raw_input().split(" ")]
	number = int(s_input[0])
	color = str(s_input[1])
	for j in range(2,number+2):
		arr[int(s_input[j])]=arr[int(s_input[j])]+1
for i in range(1,6):
    if(arr[i]==n):
        print "YES"
    elif(arr[i]==1):
        print "NO"
    else:
        print "UNDEFINED"
