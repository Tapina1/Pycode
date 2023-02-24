#Armstrong number:(ex:153-->1+125+27-->153,ex:1634-->1+1296+81+256-->1634)
#only for 3digits number)
i=int(input("Enter a number to check for Armstrong:"))
orig=i
sum=0
while i>0:
	sum=sum+(i%10)**3
	i=i//10
if orig==sum:
	print("Number is Armstrong",sum)
else:
	print("Not an Armstrong:",sum)

	"""For any no of digits"""

n=int(input("Enter a number:"))
i=n
count=0
while (i>0):
	i=i//10
	count += 1
sum=0
i=n
while i>0:
	digit = i%10
	x=1
	pro=1
	while x <= count:
		pro=pro*digit
		x+=1
	sum=sum+pro
	i=i//10
if sum == n:
	print("Armstrong")
else:
	print("Not Armstrong")
