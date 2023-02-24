i=int(input("Please Enter a number:"))
sum=0
while i>0:
	sum=sum+(i%10)**2
	i=i//10
print("Sum of square of digits:",sum)

'''OR'''
i=int(input("Please Enter a number to sum of cube of digits:"))
sum=0
while i>0:
	sum=sum+(i%10)**3
	i=i//10
print("Sum of square of digits:",sum)