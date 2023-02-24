#Practice programmes
#Wap to find sum of elements of the list
a=[]
size=int(input("Enter the range of list:"))
for i in range(size):
    val=int(input("Enter the numbers:"))
    a.append(val)
print("Elements of the list:",a)
sum=0
for i in range(size):
    sum=sum+a[i]
print("Sum of elements is",sum)