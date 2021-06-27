
def evenlist(n):
	lst=[]
	t=0
	while(n>0):
		t=n%10
		if t%2 == 0:
			lst.append(t)
		n=n//10
	
	return lst[::-1]

def oddlist(n):
	lst=[]
	t=0
	while(n>0):
		t=n%10
		if t%2 == 1:
			lst.append(t)
		n=n//10
	return lst[::-1]

def length(n):
	s=str(n)
	return len(s)		

#n=int(input())
n=457996548895
print("Given number is:",n)
print("Even numbers are:",evenlist(n))
print("Odd numbers are:",oddlist(n))
lent= length(n)
x=(10**(lent//2))
l=n//x
r=n-l*x
le=evenlist(l)
re=evenlist(r)
print("Left half of even numbers:",le)
print("Right half of even numbers:",re)
print("Sum of left even numbers is:",sum(le))
print("sum of right even numbers is:",sum(re))


