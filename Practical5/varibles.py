#4.1 Some simple math
a = 233

b = 233233

c = b/7
print (c)

d = c/11
e = d/13
    
if a > e:
    print("a > e")
elif e > a:
    print("a < e")
else:
    print("a = e")
    
#b = 1001*a
#c = 143*a
#d = 13*a
#e = a


#4.2 Booleans
for X in range(0,2):
    for Y in range(0,2):
        Z = ((X or Y) and not(X and Y)) == 1 
        W = X != Y
        print(X,Y,Z,W)

 