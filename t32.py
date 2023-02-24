n=int(input("Enter a number to get product of digits:"))
prod=1
while n>0:
	prod=prod*(n%10)
	n=n//10
print("Product of digits:",prod) 