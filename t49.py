#With giving default value in argument

def add(a,b,c=5):
	d=a+b+c
	print("Addition:",d)
add(5,6,7)
add(5,6)

#some different method
#once you put default value in argument,you have to put all the values after that in each argument
def add(a,b=6,c=5):
	d=a+b+c
	print("Addition:",d)
add(5)
add(5,7)
add(5,4,1)
add(3,4,5)
