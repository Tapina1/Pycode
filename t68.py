#remove()/delete methods in list
a=[]
for i in range(5):
    x=input("Enter value:")
    a.append(x)
print(a)
rm=input("Enter value to remove:")
a.remove(rm)
print("List after deletion:",a)