#6 operations
def op(x,y):
    r=[]
    r.append(x+y)
    r.append(x-y)
    r.append(x*y)
    r.append(y-x)
    if y!=0:
        r.append(x/y)
    if x!=0:
        r.append(y/x)
    return r

flag=False
L=list[:]
bcd=[]
abcd=[]
i=0

'''
#generate random 4 numbers
import random
list=[]
for i in range(4):
    list.append(random.randint(1,23))
print(list)
'''

#input
raw=input('''\
Please input numbers to compute 24:\
(use ',' to dicide them)
''')
list=[]
lis=raw.split(',')
for i in lis:
    list.append(int(i))
#check 1-23
for i in list:
    if i not in range(1,24):
        print('The input number must be integers from 1 to 23')
        break
else:
    
    while i<4 and not flag:
        list=L[:]
        a=list.pop(i)
        LL=list[:]
        for j in range(3):
            list=LL[:]
            b=list.pop(j)
            c=list[0]
            d=list[1]
            for k in op(c,d):  
                bcd.extend(op(b,k))
            for l in bcd:
                abcd.extend(op(a,l))
            if 24 in abcd:
                flag=True
                break
        i+=1
        
    if flag:
        print('Yes')
    else:
    	print('No')
    
    print('Recursion times: ',len(abcd))