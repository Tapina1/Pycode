#find(),islanum(),isdigit() and isspace() 
#find
x="RAM IS GOING TO MARKET"
y="TO"
print(x.find(y,0,(len(x)-1)))

#isalnum & isdigit()
a="ram123"
b="Hello"
c="12346"
d=""
e=" "
print(a.isalnum())
print(b.isalnum())
print(c.isalnum())
print(d.isalnum())

print()
print()
#isdigit
print(a.isdigit())
print(b.isdigit())
print(c.isdigit())
print(d.isdigit())
print()
#isspace()
print(c.isspace())
print(d.isspace())
print(e.isspace())


print()
print(len(a),type(a))