#Prime no:not divisible by more than two nos,only two factors,1 & no(ex:11,13,19...etc)
n=int(input("Enter a number to check prime no:"))
count=0
i=1
while i <= n:
	if n%i==0:
		count=count+1
	i+=1
if count==2:
	print("Prime Number")
else:
	print("Not Prime/Composite Number")