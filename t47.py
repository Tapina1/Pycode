# function without argument
def oddeven():
	a=int(input("Enter a number:"))
	if a%2==0:
		print("Even")
	else:
		print("Odd")
oddeven()
	
#with argument

def oddeven(a):
	if a%2==0:
		print("Even")
	else:
		print("Odd")
m=int(input("Enter a no:"))

oddeven(m)		 

