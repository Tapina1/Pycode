#Wap to find reverse of a string
a=input("Enter String:")
#print(a[-1::-1])
for i in range((len(a)-1),-1,-1):
    print(a[i],end="")

    
print()
print(len(a),type(a))