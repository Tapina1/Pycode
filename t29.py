i=int(input("Enter a number you want to add its digits:"))
sum=0
while i>0:
	sum=sum+i%10
	i=i//10
print("Sum of digitd of numbers:",sum)
