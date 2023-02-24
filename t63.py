#list methods in python(cmp()):
#RUNS ONLY in PYTHON v2.0
a1=[2,3,4,6]
a2=[2,3,4,7]
a3=[2,3,4,7,11]
a4=[2,3,4,6]
print("Comparing a1 and a2:")
print(cmp(a1,a2)) #run:-1
print(cmp(a1,a4))#run:0
print(cmp(a2,a3))#run:-1

print()
#incase of multiple datatypes
b1=[2,3,4,6]
b2=[2,3,4,"a"]
b3=["a","b","c"]
b4=['a','c','b']
print(cmp(b2,b1)) #run:1
print(cmp(b3,b4))#run:-1
print(cmp(b2,b3))#run:-1