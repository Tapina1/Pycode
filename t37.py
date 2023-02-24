n=int(input("Enter a number to print fibonicci series:"))
x=0
y=1
z=0
while z <= n:
	print(z)
	x=y
	y=z
	z=x+y