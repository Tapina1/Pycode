#Tuple: is immutable,(one created you can't modify or update its data)

#"in" membership operator
tuple1=(1,2,3,4)
for t in tuple1:
    print(t,type(tuple1))
#In range method
for t in range(len(tuple1)):
    print(tuple1[t],type(tuple1))
#joining of tuple
tuple2=(5,6,7)
tuple3=tuple1+tuple2
print(tuple3,type(tuple3))
#replicating tuple
tuple2=tuple1*3
print(tuple2,type(tuple2))
#Slicing in tuple
t1=(10,20,10,30,10,40,50,60)
t2=t1[3:5]
print(t2,type(t2))
t3=t1[0:5:2]
print(t3,type(t3))
#ALL FUNCTIONS OF TUPLE
print("Length is",len(t1),"Max value is",max(t1),"min value is",min(t1))
c=t1.index(30)
d=t1.count(10)
print("index of 30",c,"frequency of 10",d,type(t1))
#tuple coversion from string,list & dictionary
t4=['A','B','C','D']
t5=tuple(t4)
t6="TAPINA"
t7=tuple(t6)
t8={'A':1,'B':2,'C':3,'D':4}
t9=tuple(t8)
print(t6,type(t6),"Converted to",t7,type(t7))
print(t4,type(t4),"Converted to",t5,type(t5))
print(t8,type(t8),"Converted to",t9,type(t9))
#to add items in tuple,we need to convert it to list
print(t5)
t10=list(t5)
print(t10)
t10[1]='E'
t5=tuple(t10)
print(t5)
temptuple=t5
#check if items exist or not
if 'C' in t5:
    print("Yes C is there")
else: print("No C ")
#delete tuple
print(temptuple)
del temptuple
print(temptuple)







