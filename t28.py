n=int(input("Enter a number upto you want Sum first even numbers:"))
i=1
sum=0
count=1
while count <= n:
 	if i%2 == 0:
 		sum = sum+i
 		count += 1
 	i+=1
print("Sum of first even numbers:",sum)