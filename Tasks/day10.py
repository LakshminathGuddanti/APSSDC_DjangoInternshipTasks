print("Contact Application:\n 1. Enter new record\n 2. Display all records\n 3. Update Record\n 4. Delete record\n 5. Exit ")

flag=True
d={}
while(flag):
	ch = int(input())
	if ch==1:
		name = input('enter your name:')
		mbno = input('Enter Mobile No. :')
		d[name]=mbno
		pass
	elif ch==2:
		print(d)
		pass
	elif ch==3:
		name = input("Enter the name:")
		mbno = input("Enter Updated mobile Number:")
		if d.update({name:mbno}):
			print("Updated")
		else:
			print("{} Doesnot exist in contacts".format(name))
	elif ch==4:
		name = input("Enter the name:")
		if d.pop(name):
			print("{} record deleted successfully".format(name))
		else:
			print("{} Doesnot exist in contact".format(name))
			
	elif ch==5:
		flag=False
	else:
		print("Enter a valid option")
		
