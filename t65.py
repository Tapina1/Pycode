#Count() methods in list

"""a=["ram","shyam","ram","tapina","bapi","gita"]
x=a.count("ram")
x1=a.count("shyam")
print("Frequency of ram=",x)
print("Frequency of shyam=",x1)
"""
a=[]
for i in range(10):
    x=input("Enter item to add in the list:")
    a.append(x)
x=input("Enter value whose frquency you want:")
f=a.count(x)
print("Frequency of ",x,"is=",f)