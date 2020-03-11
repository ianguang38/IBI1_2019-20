from random import randint
x = randint(1,8192)

print(x)
n = x
s = ""

for i in range(1,13):
    a = n%2
    n = n//2
    if a:
        if s == "":
            s = "2**"+str(i-1)
        else:    
            s = "2**"+str(i-1)+"+"+s
    if n == 0:
        break
    

print(s)
