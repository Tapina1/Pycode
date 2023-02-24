#pop() methods in list
a=[]
for i in range(5):
    x=input("Enter values:")
    a.append(x)
print(a)
a.pop()
print("After first pop:",a)


a.pop()
print("After 2nd pop:",a)
a.pop()
print("After 3rd pop:",a)
a.pop()
print("After 4th pop:",a)
a.pop()
print("After 5th pop:",a)
#error shows,if you pop from empty list
a.pop()
print("After 6th pop:",a)


