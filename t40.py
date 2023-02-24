#star printing
k=1
i=1
while i <= 5:
    b=1
    while b <= 5-i:
        print(" ",end='')
        b += 1
    j=1
    while j <= k:
        print("*",end='')  #to print different pyramid,change '*' to i,j or k 
        j += 1
    k += 2
    print()
    i += 1
