#wap to count frequency of a given number
a=[]
x=int(input("Enter the range of list:"))
for i in range(x):
    val=int(input("Enter the numbers:"))
    a.append(val)
print("List:",a)
y=int(input("Enter the number to find frequency:"))
c=a.count(y)
print("Frequency =",c)