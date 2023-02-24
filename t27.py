n=int(input("Enter a number:"))
i=2
sum=0
while i<=n:
	sum=sum+i
	i+=2
print("Sum of even numbers:",sum)

'''OR'''
n=int(input("Enter a number upto which you want to add even numbers:"))
i=1
sum=0
while i<=n:
	if i%2 == 0:
		sum = sum+i
	i += 1
print("Sum of even numbers:",sum)