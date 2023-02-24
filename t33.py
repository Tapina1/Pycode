i=int(input("Enter a number:"))
rev=0
while i>0:
	rev=(rev*10)+(i%10)
	i=i//10
print("Reverse no is",rev)