 #No argument with return
def add():
	a=int(input("Enter 1st no:"))
	b=int(input("ENter 2nd no:"))
	c=a+b
	return c
x=add()
print("Addition:",x)

#Argument with return

def add(a,b):
	c=a+b
	return c
a=int(input("a:"))
b=int(input("b:"))
y=add(a,b)
print("Addition",y)
