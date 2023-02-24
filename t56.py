#Wap to check  string is pallindrome or not
a=input("Enter String:")
b=a[-1::-1]
if (a==b):
    print("Palindrome String")
else:
    print("Not Pallindrome String")


print()
print(len(a),type(a))