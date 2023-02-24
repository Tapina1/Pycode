#Pallindrome no:(ex:525-->rev-->525,)
i=int(input("Enter a number to check pallindrome:"))
x=i
rev=0
while i>0:
	rev=(rev*10)+(i%10)
	i=i//10
if (x == rev):
	print("No is pallindrome",rev)
else:
	print("Not pallindrome",rev)