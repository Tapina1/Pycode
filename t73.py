#Wap to count total no of odd and even in the list
a=[]
n=int(input("Enter the range:"))
for i in range(n):
    x=int(input("Enter the numbers in list:"))
    a.append(x)
print("Given list was:",a)
odd=0
even=0
for i in range(n):
    if a[i]%2==0:
        even=even+1
    else:
        odd=odd+1
print("Total no of even",even,"Total no of odd",odd)