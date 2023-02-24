a=[]
x=int(input("Enter the range of list:"))
for i in range(x):
    val=int(input("Enter the numbers:"))
    a.append(val)
print("List is",a)
a.reverse()
print("Reverse list is",a)
"""
#or
print()
i=0
j=x-1
while i<j:
    t=a[i]
    a[i]=a[j]
    a[j]=t
    i=i+1
    j=j-1
print("List after reverse=")
for i in range(x):
    print(a[i])
"""