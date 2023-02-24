#wap to search a numbers in the list
a=[]
size=int(input("Enter the size of the list:"))
for i in range(size):
   val=int(input("Enter the numbers:"))
   a.append(val)
print("Numbers in the list:",a)
key=int(input("Enter the number you want to search:"))
flag=0
for i in range(size):
    if a[i]==key:
        flag=1
        pos=i+1
        break
if flag==1:
    print("Number is found at",pos,"Position")
else:
    print("Number is not found")