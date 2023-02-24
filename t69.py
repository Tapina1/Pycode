#reverse() and sort() methods in list
a=[]
for i in range(5):
    x=input("Enter values:")
    a.append(x)
print(a)
c=a
a.reverse()
print("reverse list:",a)
c.sort()
print("after sort:",c)