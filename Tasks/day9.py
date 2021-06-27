st = input()
alpha = []
num = []
charList = []
for i in st:
	if i.isalpha() :
		alpha.append(i)
		pass
	elif i.isnumeric():
		num.append(i)
		pass
	else:
		charList.append(i)
		pass
print("Given String is:",st)
print("Alphabets in ",st," is: ",end="")
for i in alpha:
	print(i,end = " ")
print("\nNumbers in ",st," is: ",end="")
for i in num:
	print(i,end = " ")
print("\nSpecial Characters in ",st," is: ",end="")
for i in charList:
	print(i,end = " ")
	
