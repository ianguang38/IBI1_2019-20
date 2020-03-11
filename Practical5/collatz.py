#Collatz sequence
a = 54
while a%1 == 0 and a !=1:
    if a%2 == 0:
        a = a/2
    else:
        a = a*3+1
    print (a)