import math

#Sieve of erastothenes
def sieve(n):
	numbers=range(0,n+1)
	for i in range(2,int(math.ceil(n**0.5))):
		if(numbers[i]):
			for j in range(i*i,n+1,i):
				numbers[j]=0

	#removing 0 and 1 and returning a list          
	numbers.remove(1)
	prime_numbers=set(numbers)
	prime_numbers.remove(0)

	primes=list(prime_numbers)
	primes.sort()
	return primes

prime_numbers=[]
prime_numbers=sieve(100000)
#print prime_numbers
def no_of_distinct_prime_factors(n):

	count=0
	flag=0
	#print prime_numbers
	if n!=1:
		for i in prime_numbers:
			#print i
			if i>n:
				break
			if n%i==0:
				count+=1
				n=n/i
		return count
	else:
		return 1
def check_digit(n,c,l):
	i=0
	r=n
	while n!=0:
		n//=10
		i+=1
	if(i==c):
		return l.append(r)
t=raw_input()
t=int(t)
for i in range(0,t):
	l=[]
	a,b=raw_input().split()
	a=int(a)
	b=int(b)
	count=0
	for k in range(a,b+1):
		c = no_of_distinct_prime_factors(k)
		check_digit(k,c,l)
	print len(l)