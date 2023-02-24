#Print Even number

n=int(input("Enter a number:"))
i=2
while i <= n:
	print(i)
	i += 2

"""OR"""

n=int(input("Enter a number upto which you want to print even numbers:"))
i=1
while i <= n:
	if i%2 == 0:
		print(i)
	i += 1
