#insert() methods in list
a=["ram","shyam","ram","tapina","bapi","gita"]
print(a)
index=int(input("Enter value of index you want to add:"))
value=input("Enter value you want to add:")
f2=a.insert(index,value)
print("List after insertion:",a)