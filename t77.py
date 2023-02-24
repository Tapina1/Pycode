#max(),min() in a list & second min value and max value in a list
a=[]
x=int(input("Enter the range of list:"))
for i in range(x):
    val=int(input("Enter the numbers:"))
    a.append(val)
print("Max in the list:",max(a))
print("Min in the list:",min(a))
#or
"""
print()

max=a[0]
for i in range(x):
    if a[i]>max:
        max=a[i]
print("Max is",max)
#or
print()
min=a[0]
for i in range(x):
    if a[i]<min:
        min=a[i]
print("Min is",min)
"""
#second min value and max value in a list
minval=min(a)
maxval=max(a)
a.remove(minval)
a.remove(maxval)
print("2nd Min value is",min(a))
print("2nd max value is",max(a))